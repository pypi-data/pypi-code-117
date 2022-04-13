import datetime as dt
from typing import Union

from aiofile import AIOFile

DATE_FORMAT = '%Y%m%d'


def strftime(date: dt.date):
    return date.strftime(DATE_FORMAT)


def strptime(date: Union[int, str]):
    return dt.datetime.strptime(str(date), DATE_FORMAT).date()


async def get_file_body(file: Union[bytes, str]):
    if isinstance(file, bytes):
        body = file
    else:
        async with AIOFile(file, 'rb') as afp:
            # this should always return bytes because of the 'rb'
            # but the typing is wrong and throws a mypy error.
            body = await afp.read()  # type: ignore
    return body
