# Copyright 2014-2015 MongoDB, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Type codes for MongoDB servers."""

from typing import NamedTuple


class _ServerType(NamedTuple):
    Unknown: int
    Mongos: int
    RSPrimary: int
    RSSecondary: int
    RSArbiter: int
    RSOther: int
    RSGhost: int
    Standalone: int
    LoadBalancer: int


SERVER_TYPE = _ServerType(*range(9))
