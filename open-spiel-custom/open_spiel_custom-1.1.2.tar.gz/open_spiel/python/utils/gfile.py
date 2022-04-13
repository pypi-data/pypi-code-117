# Copyright 2019 DeepMind Technologies Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This is replaces google's gfile used for network storage.

A more complete public version of gfile:
https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/platform/gfile.py
"""

import os

# pylint: disable=invalid-name
Exists = os.path.exists
IsDirectory = os.path.isdir
ListDir = os.listdir
MakeDirs = os.makedirs
Open = open
