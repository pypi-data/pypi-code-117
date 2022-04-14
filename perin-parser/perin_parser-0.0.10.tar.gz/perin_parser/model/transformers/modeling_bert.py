# coding=utf-8
# Copyright 2018 The Google AI Language Team Authors and The HuggingFace Inc. team.
# Copyright (c) 2018, NVIDIA CORPORATION.  All rights reserved.
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
"""PyTorch BERT model. """

import torch
import torch.utils.checkpoint


# ugly hack against "None of the inputs have requires_grad=True. Gradients will be None"
def checkpoint(module, *args, **kwargs):
    dummy = torch.empty(1, requires_grad=True)
    return torch.utils.checkpoint.checkpoint(lambda d, *a, **k: module(*a, **k), dummy, *args, **kwargs)
