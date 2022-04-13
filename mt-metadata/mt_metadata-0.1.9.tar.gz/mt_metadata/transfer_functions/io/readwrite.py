# -*- coding: utf-8 -*-
"""
This is a utility function to get the appropriate reader for a given file type and 
return the appropriate object of :class:`mth5.timeseries`

This setup to be like plugins but a hack cause I did not find the time to set
this up properly as a true plugin.  

If you are writing your own reader you need the following structure:
    
    * Class object that will read the given file
    * a reader function that is read_{file_type}, for instance read_nims
    * the return value is a :class:`mtpy.core.mt.MT`
    
    :rubric:
        
        class NewFile
            def __init__(self, fn):
                self.fn = fn
            
            def read_header(self):
                return header_information
            
            def read_newfile(self):
                ex, ey, hx, hy, hz = read_in_channels_as_MTTS
                return RunTS([ex, ey, hx, hy, hz])
            
        def read_newfile(fn):
            new_file_obj = NewFile(fn)
            run_obj = new_file_obj.read_newfile()
            
            return run_obj, extra_metadata
        
Then add your reader to the reader dictionary so that those files can be read.
        
.. seealso:: Existing readers for some guidance.

Created on Wed Aug 26 10:32:45 2020

:author: Jared Peacock

:license: MIT

"""
# =============================================================================
# Imports
# =============================================================================

from pathlib import Path

from mt_metadata.utils.mt_logger import setup_logger
from mt_metadata.transfer_functions.io import (
    read_edi,
    write_edi,
    read_zmm,
    write_zmm,
    read_jfile,
    write_jfile,
    read_emtfxml,
    write_emtfxml,
    read_avg,
    write_avg,
)

logger = setup_logger(__name__)
# =============================================================================
# generic reader for any file type
# =============================================================================
plugins = {
    "edi": {"file_types": ["edi"], "reader": read_edi, "writer": write_edi},
    "zmm": {
        "file_types": ["zmm", "zrr", "zss"],
        "reader": read_zmm,
        "writer": write_zmm,
    },
    "j": {"file_types": ["j"], "reader": read_jfile, "writer": write_jfile,},
    "emtfxml": {
        "file_types": ["xml"],
        "reader": read_emtfxml,
        "writer": write_emtfxml,
    },
    "avg": {"file_types": ["avg"], "reader": read_avg, "writer": write_avg,},
}


def get_reader(extension):
    """

    get the proper reader for file extension

    :param extension: file extension
    :type extension: string
    :return: the correct function to read the file
    :rtype: function

    """

    for key, vdict in plugins.items():
        if extension.lower() in vdict["file_types"]:
            return key, vdict["reader"]

    msg = f"Could not find a reader for file type {extension}"
    logger.error(msg)
    raise ValueError(msg)


def get_writer(extension):
    """

    get the proper reader for file extension

    :param extension: file extension
    :type extension: string
    :return: the correct function to read the file
    :rtype: function

    """

    for key, vdict in plugins.items():
        if extension.lower() in vdict["file_types"]:
            return key, vdict["writer"]

    msg = f"Could not find a writer for file type {extension}"
    logger.error(msg)
    raise ValueError(msg)


def read_file(fn, file_type=None):
    """

    :param fn: full path to file
    :type fn: string or :class:`pathlib.Path`
    :param string file_type: a specific file time if the extension is ambiguous.
    :return: MT time series object
    :rtype: :class:`mth5.timeseries.MTTS`

    """

    if not isinstance(fn, Path):
        fn = Path(fn)

    if not fn.exists():
        msg = f"Could not find file {fn}. Check path."
        logger.error(msg)
        raise IOError(msg)

    if file_type is not None:
        try:
            file_reader = plugins[file_type]["reader"]
        except KeyError:
            msg = (
                f"Reader for the file type {file_type} does not currently exist. "
                f"Current readers {list(plugins.keys())}"
            )
            logger.error(msg)
            raise KeyError(msg)
    else:
        file_type, file_reader = get_reader(fn.suffix.replace(".", ""))

    return file_reader(fn)


def write_file(mt_object, fn, file_type=None, **kwargs):
    """
    write a file based on extension or file type

    :param fn: DESCRIPTION
    :type fn: TYPE
    :param file_type: DESCRIPTION, defaults to None
    :type file_type: TYPE, optional
    :return: DESCRIPTION
    :rtype: TYPE

    longitude_format="lon",
    latlon_format="dms",
    overwrite=False,

    """

    if not isinstance(fn, Path):
        fn = Path(fn)

    if file_type is not None:
        try:
            file_writer = plugins[file_type]["writer"]
        except KeyError:
            msg = (
                f"Writer for the file type {file_type} does not currently exist. "
                f"Current writers {list(plugins.keys())}"
            )
            logger.error(msg)
            raise KeyError(msg)
    else:
        file_type, file_writer = get_writer(fn.suffix.replace(".", ""))

    new_obj = file_writer(mt_object, fn, **kwargs)
    logger.info("Wrote %s", fn)

    return new_obj
