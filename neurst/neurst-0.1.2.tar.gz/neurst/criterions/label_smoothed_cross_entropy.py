# Copyright 2020 ByteDance Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import tensorflow as tf
from absl import logging

from neurst.criterions import register_criterion
from neurst.criterions.criterion import Criterion
from neurst.metrics.metric import MetricWrapper
from neurst.models.model_utils import input_length_to_nonpadding
from neurst.utils.compat import is_tf_tensor
from neurst.utils.flags_core import Flag
from neurst.utils.misc import to_numpy_or_python_type


@register_criterion
class LabelSmoothedCrossEntropy(Criterion):

    def __init__(self, args):
        """ Initializes the cross entropy with label smoothing.

        Args:
            args: A dict of full parameters.
        """
        super(LabelSmoothedCrossEntropy, self).__init__()
        self._label_smoothing = args["label_smoothing"]
        if self._label_smoothing > 0:
            logging.info("Using LabelSmoothedCrossEntropy with label_smoothing={}".format(self._label_smoothing))

    @staticmethod
    def class_or_method_args():
        """ Returns a list of args for flag definition. """
        return [Flag("label_smoothing", dtype=Flag.TYPE.FLOAT,
                     default=0., help="The label smoothing constant.")]

    def reduce_loss(self, model_inp, model_out):
        """ Reduces loss tensor for training according to the model inputs
            and outputs.

        Returns: A float tensor.
        """
        nll_sum, n_samples, n_tokens = self(model_inp, model_out)
        return tf.reduce_sum(nll_sum) / tf.reduce_sum(n_tokens)

    def reduce_metrics(self, eval_res_list) -> dict:
        """ Reduces the metrics according to a list of returned value from `eval`.

        Args:
            eval_res_list: A list of tuples of numpy.ndarray generated by `self.__call__`
                and model.__call__.

        Returns:
            A dict of reduced metrics for evaluation.
        """
        nll_sum, nll_samples, nll_tokens = 0., 0., 0.
        for _nll_sum, _nll_samples, _nll_tokens in eval_res_list:
            nll_sum += tf.reduce_sum(_nll_sum)
            nll_samples += tf.reduce_sum(_nll_samples)
            nll_tokens += tf.reduce_sum(_nll_tokens)
        nll = nll_sum / nll_samples
        ppl = 2. ** (nll_sum / nll_tokens)
        return {"NLL": nll, "PPL": ppl}

    def reduce_sample_metrics(self, eval_res):
        """ Reduces the metrics at sample level.

        Args:
            eval_res: A tuple of numpy.ndarray or tensors generated by `self.__call__`.

        Returns:
            A list of dict of reduced metrics (scalar) for evaluation.
        """
        nll_sum, _, nll_tokens = eval_res
        nll_sum = to_numpy_or_python_type(nll_sum)
        nll_tokens = to_numpy_or_python_type(nll_tokens)
        return [{"nll": _nll, "ppl": 2. ** (_nll / _tokens),
                 "nll_per_token": _nll / _tokens}
                for _nll, _tokens in zip(nll_sum, nll_tokens)]

    def as_metric(self):
        """ Returns a wrapper class of Metric. """
        return MetricWrapper(flag="NLL", greater_is_better=False)

    def __call__(self, model_inp, model_out):
        """ Calculates.

        Args:
            model_inp: A dict containing the model inputs.
            model_out: The logits tensor or a dict containing the logits tensor.
                The logits tensor with shape [batch, max_len, vocab_size].

        Returns:
            The (nll_sum, num_of_samples(batch), num_of_tokens) with shape:
            nll_sum: [batch_size, ]
            num_of_samples: [1, ],
            num_of_tokens: [batch_size, ]
        """
        logits = model_out
        if isinstance(model_out, dict):
            logits = model_out["logits"]
        elif not is_tf_tensor(model_out):
            raise ValueError("Not supported type of model_out: {}".format(type(model_out)))

        logits = tf.cast(logits, tf.float32)
        labels = model_inp["trg"]

        with tf.name_scope("loss"):
            vocab_size = logits.get_shape()[-1]
            confidence = 1.0 - self._label_smoothing
            low_confidence = self._label_smoothing / tf.cast(vocab_size - 1, tf.float32)
            soft_target = tf.one_hot(
                tf.cast(labels, tf.int32),
                depth=vocab_size,
                on_value=confidence,
                off_value=low_confidence)
            # this may cause NaN when meets bad sample
            xentropy = tf.nn.softmax_cross_entropy_with_logits(
                logits=logits, labels=soft_target)
            # xentropy = - tf.reduce_sum(soft_target * tf.nn.log_softmax(logits), axis=-1)
            # Calculate the best (lowest) possible value of cross entropy, and
            # subtract from the cross entropy loss.
            if self._label_smoothing:
                normalizing_constant = -(
                    confidence * tf.math.log(confidence)
                    + tf.cast(vocab_size - 1, tf.float32) * low_confidence
                    * tf.math.log(low_confidence + 1e-20))
                xentropy -= normalizing_constant
            # else:
            # TODO(ZhaoChengqi) https://github.com/tensorflow/tensorflow/issues/32578
            # xentropy = tf.nn.sparse_softmax_cross_entropy_with_logits(
            #     logits=logits, labels=labels)
            padding = model_inp.get("trg_padding", None)
            if padding is None:
                padding = model_inp.get("padding", None)
            length = model_inp.get("trg_length", None)
            if length is None:
                length = model_inp.get("length", None)
            if padding is None:
                weights = input_length_to_nonpadding(length, tf.shape(labels)[1], tf.float32)
            else:
                weights = tf.cast(1 - padding, tf.float32)
            if model_inp.get("mask", None) is not None:
                weights = weights * tf.cast(model_inp["mask"], tf.float32)
            nll_sum = tf.reduce_sum(xentropy * weights, axis=1)
            n_samples = tf.cast(tf.expand_dims(tf.shape(labels)[0], axis=0), dtype=tf.float32)
            n_tokens = tf.reduce_sum(weights, axis=1)
            return nll_sum, n_samples, n_tokens
