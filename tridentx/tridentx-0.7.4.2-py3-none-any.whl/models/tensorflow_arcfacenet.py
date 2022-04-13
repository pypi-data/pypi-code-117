from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import inspect
import math
import os
import uuid
from collections import *
from collections import deque
from copy import copy, deepcopy
from functools import partial
from itertools import repeat

import numpy as np

import tensorflow as tf
from trident.models.pretrained_utils import _make_recovery_model_include_top

from trident.backend.common import *
from trident.backend.tensorflow_backend import *
from trident.backend.tensorflow_ops import *
from trident.data.image_common import *
from trident.data.utils import download_model_from_google_drive,download_file_from_google_drive
from trident.layers.tensorflow_activations import get_activation, Identity, Relu,PRelu
from trident.layers.tensorflow_blocks import *
from trident.layers.tensorflow_layers import *
from trident.layers.tensorflow_normalizations import get_normalization, BatchNorm,BatchNorm2d
from trident.layers.tensorflow_pooling import GlobalAvgPool2d, MaxPool2d
from trident.optims.tensorflow_trainer import *
from trident.data.vision_transforms import Resize,Normalize

__all__ = ['SEResNet_IR','load','BottleNeck_IR_SE','BottleNeck_IR','SEResNet_IR_50_512']

_session = get_session()
_device = get_device()
_epsilon=_session.epsilon
_trident_dir=_session.trident_dir
_backend = get_backend()

dirname = os.path.join(_trident_dir, 'models')
if not os.path.exists(dirname):
    try:
        os.makedirs(dirname)
    except OSError:
        # Except permission denied and potential race conditions
        # in multi-threaded environments.
        pass






def BottleNeck_IR(num_filters, strides,keep_filter=True):
    blocks = OrderedDict()
    blocks['res_layer'] = Sequential(BatchNorm2d(),
                                     Conv2d_Block((3, 3), num_filters=num_filters, strides=1, auto_pad=True, use_bias=False, activation=PRelu(num_filters)),
                                     Conv2d_Block((3, 3), num_filters, strides=strides, use_bias=False, activation=None,  normalization='batch'))
    if keep_filter:
        blocks['shortcut_layer']=MaxPool2d(1, strides=strides,name='shortcut_layer')
    else:
        blocks['shortcut_layer'] = Conv2d_Block((1, 1), num_filters, strides=strides, use_bias=False, activation=None, normalization='batch')
    return ShortCut2d(blocks,mode='add')

def BottleNeck_IR_SE( num_filters, strides,keep_filter=True):
    blocks = OrderedDict()
    blocks['res_layer'] = Sequential(BatchNorm2d(),
                                     Conv2d_Block((3, 3), num_filters=num_filters, strides=1, auto_pad=True, use_bias=False, activation=PRelu(num_filters)),
                                     Conv2d_Block((3, 3), num_filters, strides=strides, use_bias=False, activation=None, normalization='batch'),
                                     SqueezeExcite(num_filters//16,num_filters),name='res_layer')
    if keep_filter:
        blocks['shortcut_layer'] = MaxPool2d(1, strides=strides, name='shortcut_layer')

    else:
        blocks['shortcut_layer'] =Conv2d_Block((1, 1), num_filters, strides=strides, use_bias=False, activation=None, normalization='batch',name='shortcut_layer')
    return ShortCut2d(blocks,mode='add')


def get_block(Bottleneck, out_channel, num_units, strides=2,keep_filter=True):
    blocks=[Bottleneck(out_channel, strides,keep_filter)]
    for i in range(num_units - 1):
        blocks.append(Bottleneck(out_channel, 1,True))
    return blocks



def SEResNet_IR(include_top=True,num_layers=50,Bottleneck=BottleNeck_IR_SE,drop_ratio=0.4,feature_dim=128,input_shape=(112,112,3)):
    blocks=OrderedDict()
    blocks['input_layer']=Conv2d_Block((3,3),64,strides=1,auto_pad=True,use_bias=False,activation=PRelu(64),normalization='batch',name='input_layer')
    blocks['body']=Sequential(
        get_block(Bottleneck, out_channel=64, num_units=3,keep_filter=True)+
        get_block(Bottleneck, out_channel=128, num_units=4,keep_filter=False)+
        get_block(Bottleneck, out_channel=256, num_units=14,keep_filter=False)+
        get_block(Bottleneck, out_channel=512, num_units=3,keep_filter=False)
    )
    blocks['output_layer']=Sequential(
        BatchNorm2d(),
        Dropout(drop_ratio),
        Flatten(),
        Dense(feature_dim),
        BatchNorm(),
        name='output_layer'
    )
    facenet=Sequential(blocks).to(_device)
    facenet.name=camel2snake('SEResNet_IR')
    model=FaceRecognitionModel(input_shape=input_shape,output=facenet)
    model.preprocess_flow=[Resize((input_shape[0],input_shape[1]),keep_aspect=True),Normalize(0,255),Normalize([0.485, 0.456, 0.406],[0.229, 0.224, 0.225])]
    #model.summary()
    return model


def SEResNet_IR_50_512(include_top=True,
             pretrained=True,
             freeze_features=True,
             input_shape=(112,112,3),
             classes=1000,
             **kwargs):
    if input_shape is not None and len(input_shape)==3:
        input_shape=tuple(input_shape)
    else:
        input_shape=(112, 112,3)
    seresnet = SEResNet_IR(include_top=include_top,num_layers=50,Bottleneck=BottleNeck_IR_SE,drop_ratio=0.4,feature_dim=512,input_shape=input_shape)
    # if pretrained:
    #     pass
    #     download_model_from_google_drive('1aLYbFvtvsV2gQ16D_vwzrKdbCgij7IoZ', dirname, 'arcface_se_50_512.pth')
    #     recovery_model = load(os.path.join(dirname, 'arcface_se_50_512.pth'))
    #     recovery_model = fix_layer(recovery_model)
    #     recovery_model.name = 'arcface_se_50_512'
    #     recovery_model = _make_recovery_model_include_top(recovery_model, include_top=include_top, classes=classes, freeze_features=freeze_features)
    #     seresnet.model = recovery_model
    # else:
    seresnet.model = _make_recovery_model_include_top(seresnet.model, include_top=include_top, classes=classes, freeze_features=True)
    seresnet.model.input_shape = input_shape
    seresnet.model.to(_device)
    return seresnet




