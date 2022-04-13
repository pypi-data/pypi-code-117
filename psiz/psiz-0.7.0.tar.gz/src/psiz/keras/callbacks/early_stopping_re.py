# -*- coding: utf-8 -*-
# Copyright 2020 The PsiZ Authors. All Rights Reserved.
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
# ============================================================================
"""Module of custom TensorFlow callbacks.

Classes:
    EarlyStoppingRe:

"""

from tensorflow.keras import callbacks


class EarlyStoppingRe(callbacks.EarlyStopping):
    """Custom early stopping.

    Args:
        See tf.keras.callbacks.EarlyStopping.

    """

    def reset(self, restart=None):
        """Reset best weights.

        Args:
            restart (optional): An integer indicating the restart
                number. This argument is not currently used, but
                that may change in later versions.

        """
        # pylint: disable=unused-argument
        self.best_weights = None
