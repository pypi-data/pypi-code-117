# Copyright (c) Microsoft Corporation.
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

from typing import Dict

from playwright._impl._connection import ChannelOwner
from playwright._impl._helper import locals_to_params


class Dialog(ChannelOwner):
    def __init__(
        self, parent: ChannelOwner, type: str, guid: str, initializer: Dict
    ) -> None:
        super().__init__(parent, type, guid, initializer)

    def __repr__(self) -> str:
        return f"<Dialog type={self.type} message={self.message} default_value={self.default_value}>"

    @property
    def type(self) -> str:
        return self._initializer["type"]

    @property
    def message(self) -> str:
        return self._initializer["message"]

    @property
    def default_value(self) -> str:
        return self._initializer["defaultValue"]

    async def accept(self, promptText: str = None) -> None:
        await self._channel.send("accept", locals_to_params(locals()))

    async def dismiss(self) -> None:
        await self._channel.send("dismiss")
