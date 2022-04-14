# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import shutil
from os.path import join, expanduser, isdir
from ovos_utils.configuration import is_using_xdg, get_xdg_base, get_xdg_config_save_path


class FileSystemAccess:
    """A class for providing access to the mycroft FS sandbox.

    Intended to be attached to skills at initialization time to provide a
    skill-specific namespace.
    """

    def __init__(self, path):
        #: Member value containing the root path of the namespace
        self.path = self.__init_path(path)

    @staticmethod
    def __init_path(path):
        if not isinstance(path, str) or len(path) == 0:
            raise ValueError("path must be initialized as a non empty string")

        path = expanduser(f'~/.{get_xdg_base()}/{path}')

        if is_using_xdg():
            xdg_path = expanduser(f'{get_xdg_config_save_path()}/{path}')
            # Migrate from the old location if it still exists
            if isdir(path) and not isdir(xdg_path):
                shutil.move(path, xdg_path)

        if not isdir(path):
            os.makedirs(path)
        return path

    def open(self, filename, mode):
        """Open a file in the provided namespace.

        Get a handle to a file (with the provided mode) within the
        skill-specific namespace.

        Parameters:
            filename (str): a path relative to the namespace.
                      subdirs not currently supported.

            mode (str): a file handle mode

        Returns:
            an open file handle.
        """
        file_path = join(self.path, filename)
        return open(file_path, mode)

    def exists(self, filename):
        """Check if file exists in the namespace.

        Args:
            filename (str): a path relative to the namespace.
                      subdirs not currently supported.
        Returns:
            bool: True if file exists, else False.
        """
        return os.path.exists(join(self.path, filename))
