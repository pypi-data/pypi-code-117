"""Jobs."""

# The code below is subject to the license contained in the LICENSE file, which is part of the source code.

from __future__ import annotations

import asyncio
import copy
import email.utils
import hashlib
import html
import json
import logging
import os
import re
import subprocess
import sys
import textwrap
import time
import warnings
from ftplib import FTP  # nosec: B402
from http.client import responses as response_names
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, TYPE_CHECKING, Union
from urllib.parse import parse_qsl, quote, SplitResult, SplitResultBytes, urldefrag, urlencode, urlparse, urlsplit

import html2text
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.structures import CaseInsensitiveDict

from . import __user_agent__
from .filters import FilterBase
from .util import TrackSubClasses

# https://stackoverflow.com/questions/39740632
if TYPE_CHECKING:
    from typing import Literal  # not available in Python < 3.8

    from .handler import JobState
    from .storage import Config

# required to suppress warnings with 'ssl_no_verify: true'
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # type: ignore[attr-defined,no-untyped-call]

logger = logging.getLogger(__name__)

DEFAULT_CHROMIUM_REVISION = {
    'linux': 885292,  # https://chromium.cypress.io/linux/stable/92.0.4515.131
    'win64': 885298,  # https://chromium.cypress.io/win64/stable/92.0.4515.131
    'win32': 885290,  # https://chromium.cypress.io/win/stable/92.0.4515.131
    'mac': 885289,  # https://chromium.cypress.io/mac/stable/92.0.4515.131
}


class NotModifiedError(Exception):
    """Raised when an HTTP 304 response status code (Not Modified client redirection) is received or the strong
    validation ETag matches the previous one; this indicates that there was no change in content."""

    ...


class BrowserResponseError(Exception):
    """Raised by 'url' jobs with 'use_browser: true' (i.e. using Pyppeteer) when a HTTP error response status code is
    received."""

    def __init__(self, args: Tuple[Any, ...], status_code: Optional[int]) -> None:
        """

        :param args: Tuple with the underlying error args, typically a string with the error text.
        :param status_code: The HTTP status code received.
        """
        Exception.__init__(self)
        self.args = args
        self.status_code = status_code

    def __str__(self) -> str:
        if self.status_code:
            return (
                f'{self.__class__.__name__}: Received response HTTP {self.status_code} '
                f'{response_names[self.status_code]}'
            )
        else:
            return self.args[0]


class JobBase(object, metaclass=TrackSubClasses):
    """The base class for Jobs."""

    __subclasses__: Dict[str, 'JobBase'] = {}
    __anonymous_subclasses__: List['JobBase'] = []

    __kind__: str = ''  # no longer set at the subclass level
    __required__: Tuple[str, ...]
    __optional__: Tuple[str, ...]

    index_number: int = 0  # added at job loading

    # __required__ in derived classes
    url: str = ''
    command: str = ''
    use_browser: Optional[bool] = False

    # __optional__ in derived classes
    _beta_use_playwright: Optional[bool] = None
    _delay: Optional[float] = None
    additions_only: Optional[bool] = None
    block_elements: List[str] = []  # Pyppeteer only
    chromium_revision: Optional[Union[Dict[str, int], Dict[str, str], str, int]] = None
    contextlines: Optional[int] = None
    cookies: Optional[Dict[str, str]] = None
    data: Union[str, Dict[str, str]] = None  # type: ignore[assignment]
    deletions_only: Optional[bool] = None
    diff_filter: Union[str, List[Union[str, Dict[str, Any]]]] = None  # type: ignore[assignment]
    diff_tool: Optional[str] = None
    encoding: Optional[str] = None
    filter: Union[str, List[Union[str, Dict[str, Any]]]] = None  # type: ignore[assignment]
    headers: Optional[Union[dict, CaseInsensitiveDict]] = None
    http_proxy: Optional[str] = None
    https_proxy: Optional[str] = None
    ignore_cached: Optional[bool] = None
    ignore_connection_errors: Optional[bool] = None
    ignore_dh_key_too_small: Optional[bool] = None
    ignore_http_error_codes: Optional[bool] = None
    ignore_https_errors: Optional[bool] = None
    ignore_timeout_errors: Optional[bool] = None
    ignore_too_many_redirects: Optional[bool] = None
    initialization_js: Optional[str] = None  # Playwright
    initialization_url: Optional[str] = None  # Playwright
    is_markdown: Optional[bool] = None
    kind: Optional[str] = None  # hooks.py
    loop: Optional[asyncio.AbstractEventLoop] = None
    markdown_padded_tables: Optional[bool] = None
    max_tries: Optional[int] = None
    method: Optional[Literal['GET', 'OPTIONS', 'HEAD', 'POST', 'PUT', 'PATCH', 'DELETE']] = None
    monospace: Optional[bool] = None
    name: Optional[str] = None
    navigate: Optional[str] = None  # backwards compatibility (deprecated)
    no_redirects: Optional[bool] = None
    note: Optional[str] = None
    referer: Optional[str] = None  # Playwright
    ssl_no_verify: Optional[bool] = None
    stderr: Optional[str] = None  # ShellJob backwards compatibility (not used)
    switches: Optional[List[str]] = None
    timeout: Optional[float] = None
    user_data_dir: Optional[str] = None
    user_visible_url: Optional[str] = None
    wait_for: Optional[Union[int, str]] = None  # pyppeteer only?
    wait_for_function: Optional[str] = None  # Playwright
    wait_for_navigation: Optional[Union[str, Tuple[str, ...]]] = None  # pyppeteer only?
    wait_for_selector: Optional[str] = None  # Playwright
    wait_for_url: Optional[str] = None  # Playwright
    wait_until: Optional[
        Literal['load', 'domcontentloaded', 'networkidle0', 'networkidle2']  # literal for pyppeteer
    ] = None

    def __init__(self, **kwargs: Any) -> None:
        # Fail if any required keys are not provided
        for k in self.__required__:
            if k not in kwargs:
                raise ValueError(
                    f"Job {self.index_number}: Required directive '{k}' missing: '{kwargs}'"
                    f' ({self.get_indexed_location()})'
                )

        for k, v in list(kwargs.items()):
            setattr(self, k, v)

    @classmethod
    def job_documentation(cls) -> str:
        """Generates simple jobs documentation for use in the --features command line argument.

        :returns: A string to display.
        """
        result = []
        for sc in TrackSubClasses.sorted_by_kind(cls):
            if sc.__doc__:
                result.append(f'  * {sc.__kind__} - {sc.__doc__}')
            else:
                result.append(f'  * {sc.__kind__}')

            for msg, value in (('    Required: ', sc.__required__), ('    Optional: ', sc.__optional__)):
                if value:
                    values = ('\n' + (len(msg) * ' ')).join(textwrap.wrap(', '.join(value), 79 - len(msg)))
                    result.append(f'{msg}{values}')
            result.append('')
        return '\n'.join(result)

    def get_location(self) -> str:
        """Get the 'location' of a job, i.e. the URL or command.

        :returns: A string with user_visible_url or the URL or command of the job.
        """
        raise NotImplementedError()

    def get_indexed_location(self) -> str:
        """Get the job number plus its 'location', i.e. the URL or command. Typically used in error displays.

        :returns: A string with the job number and the URL or command of the job.
        """
        raise NotImplementedError()

    def pretty_name(self) -> str:
        """Get the 'pretty name' of a job, i.e. either its 'name' (if defined) or the 'location' (URL or command).

        :returns: A string with the 'pretty name' the job.
        """
        raise NotImplementedError()

    def serialize(self) -> dict:
        """Serialize the Job object, excluding its index_number (e.g. for saving).

        :returns: A dict with the Job object serialized.
        """
        d = self.to_dict()
        d.pop('index_number', None)
        return d

    @classmethod
    def unserialize(cls, data: dict) -> 'JobBase':
        """Unserialize a dict with job data (e.g. from the YAML jobs file) into a JobBase type object.

        :param data: The dict with job data (e.g. from the YAML jobs file).
        :returns: A JobBase type object.
        """
        # Backwards compatibility with 'navigate' directive (deprecated)
        if data.get('navigate') and not data.get('use_browser'):
            warnings.warn(
                f"Job directive 'navigate' is deprecated: replace with 'url' and add 'use_browser: true' ({data})",
                DeprecationWarning,
            )
            data['url'] = data.get('url', data['navigate'])
            data['use_browser'] = True

        if 'kind' in data:
            # Used for hooks.py.
            try:
                job_subclass = cls.__subclasses__[data['kind']]
            except KeyError:
                raise ValueError(f"Job directive 'kind' ({data['kind']}) does not match any known job kinds:\n{data}")
        else:
            # Auto-detect the job subclass based on required directives.
            matched_subclasses = [
                subclass
                for subclass in list(cls.__subclasses__.values())[1:]
                if all(data.get(required) for required in subclass.__required__)
            ]
            if len(matched_subclasses) == 1:
                job_subclass = matched_subclasses[0]
            elif len(matched_subclasses) > 1:
                number_matched: Dict[JobBase, int] = {}
                for match in matched_subclasses:
                    number_matched[match] = [data.get(required) is not None for required in match.__required__].count(
                        True
                    )
                # noinspection PyUnresolvedReferences
                job_subclass = sorted(number_matched.items(), key=lambda x: x[1], reverse=True)[0][0]
            else:
                if len(data) == 1:
                    raise ValueError(
                        f"Job directive has no value or doesn't match a job type; check for errors/typos/escaping:\n"
                        f'{data}'
                    )
                else:
                    raise ValueError(
                        f"Job directives (with values) don't match a job type; check for errors/typos/escaping:\n{data}"
                    )

        # Remove extra required directives ("Falsy")
        other_subclasses = list(cls.__subclasses__.values())[1:]
        other_subclasses.remove(job_subclass)
        for other_subclass in other_subclasses:
            for k in other_subclass.__required__:
                if k not in job_subclass.__required__:
                    data.pop(k, None)

        return job_subclass.from_dict(data)

    def to_dict(self) -> dict:
        """Return all defined Job object directives (required and optional) as a serializable dict.

        :returns: A dict with all job directives as keys, ignoring those that are extras.
        """
        return {
            k: dict(getattr(self, k)) if isinstance(getattr(self, k), CaseInsensitiveDict) else getattr(self, k)
            for keys in (self.__required__, self.__optional__)
            for k in keys
            if getattr(self, k) is not None
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'JobBase':
        """Create a JobBase class from a dict, checking that all keys are recognized (i.e. listed in __required__ or
        __optional__).

        :param data: Job data in dict format (e.g. from the YAML jobs file).
        :returns: A JobBase type object.
        """
        for k in data.keys():
            if k not in (cls.__required__ + cls.__optional__):
                raise ValueError(f"Job directive '{k}' is unrecognized; check for errors/typos/escaping:\n{data}")
        return cls(**{k: v for k, v in list(data.items())})

    def __repr__(self) -> str:
        """Represent the Job object as a string.

        :returns: A string representing the Job.
        """
        return f'<{self.__kind__} {" ".join(f"{k}={v!r}" for k, v in list(self.to_dict().items()))}'

    def _dict_deep_merge(self, source: Union[dict, CaseInsensitiveDict], destination: dict) -> dict:
        """Deep merges source dict into destination dict.

        :param source: The source dict.
        :param destination: The destination dict.
        :returns: The merged dict.
        """
        # https://stackoverflow.com/a/20666342
        for key, value in source.items():
            if isinstance(value, (dict, CaseInsensitiveDict)):
                # get node or create one
                node = destination.setdefault(key, {})
                self._dict_deep_merge(value, node)
            else:
                destination[key] = value

        return destination

    def _set_defaults(self, defaults: Optional[Dict[str, Any]]) -> None:
        """Merge default attributes (e.g. from configuration) into those of the Job object.

        :param defaults: The default Job parameters.
        """

        if isinstance(defaults, dict):
            # merge defaults from configuration (including dicts) into Job attributes without overwriting them
            for key, value in defaults.items():
                if key in self.__optional__:
                    if getattr(self, key) is None:
                        setattr(self, key, value)
                    elif isinstance(defaults[key], (dict, CaseInsensitiveDict)) and isinstance(
                        getattr(self, key), (dict, CaseInsensitiveDict)
                    ):
                        for subkey, subvalue in defaults[key].items():
                            if hasattr(self, key) and subkey not in getattr(self, key):
                                getattr(self, key)[subkey] = subvalue

    def with_defaults(self, config: Config) -> 'JobBase':
        """Obtain a Job object that also contains defaults from the configuration.

        :param config: The configuration as a dict.
        :returns: A JobBase object.
        """
        job_with_defaults = copy.deepcopy(self)
        if job_with_defaults.headers:
            if not isinstance(job_with_defaults.headers, dict):
                raise ValueError(
                    f"Error reading jobs file: 'headers' directive must be a dictionary in job "
                    f'{job_with_defaults.url or job_with_defaults.command}'
                )
            job_with_defaults.headers = CaseInsensitiveDict(job_with_defaults.headers)
        cfg = config.get('job_defaults')
        if isinstance(cfg, dict):
            if 'headers' in cfg.get('all', {}):
                cfg['all']['headers'] = CaseInsensitiveDict(cfg['all']['headers'])
            if 'headers' in cfg.get('url', {}):
                cfg['url']['headers'] = CaseInsensitiveDict(cfg['url']['headers'])
            if 'headers' in cfg.get('browser', {}):
                cfg['browser']['headers'] = CaseInsensitiveDict(cfg['browser']['headers'])
            job_with_defaults._set_defaults(cfg.get(self.__kind__))  # type: ignore[arg-type]
            job_with_defaults._set_defaults(cfg.get('all'))
        return job_with_defaults

    def get_guid(self) -> str:
        """Calculate the GUID, currently a simple SHA1 hash of the location (URL or command).

        :returns: the GUID.
        """
        location = self.get_location()
        return hashlib.sha1(location.encode()).hexdigest()  # nosec: B303

    def retrieve(self, job_state: JobState, headless: bool = True) -> Tuple[Union[str, bytes], str]:
        """Runs job to retrieve the data, and returns data and ETag.

        :param job_state: The JobState object, to keep track of the state of the retrieval.
        :param headless: For browser-based jobs, whether headless mode should be used.
        :returns: The data retrieved and the ETag.
        """
        raise NotImplementedError()

    def main_thread_enter(self) -> None:
        """Called from the main thread before running the job. No longer needed (does nothing)."""
        ...

    def main_thread_exit(self) -> None:
        """Called from the main thread after running the job. No longer needed (does nothing)."""
        ...

    def format_error(self, exception: Exception, tb: str) -> str:
        """Format the error of the job if one is encountered.

        :param exception: The exception.
        :param tb: The traceback.
        :returns: A string to display and/or use in reports.
        """
        return tb

    def ignore_error(self, exception: Exception) -> Union[bool, str]:
        """Determine whether the error of the job should be ignored.

        :param exception: The exception.
        :returns: True or the string with the number of the HTTPError code if the error should be ignored,
           False otherwise.
        """
        return False


class Job(JobBase):
    """Job class for jobs."""

    __required__: Tuple[str, ...] = ()
    __optional__: Tuple[str, ...] = (
        'kind',  # hooks.py
        'index_number',
        'name',
        'note',
        'additions_only',
        'contextlines',
        'deletions_only',
        'diff_filter',
        'diff_tool',
        'filter',
        'markdown_padded_tables',
        'max_tries',
        'monospace',
        'is_markdown',
        'user_visible_url',
    )

    def get_location(self) -> str:
        """Get the 'location' of a job, i.e. the URL or command.

        :returns: A string with user_visible_url or the URL or command of the job.
        """
        pass

    def get_indexed_location(self) -> str:
        """Get the job number plus its 'location', i.e. the URL or command. Typically used in error displays.

        :returns: A string with the job number and the URL or command of the job.
        """
        return f'Job {self.index_number}: {self.get_location()}'

    def pretty_name(self) -> str:
        """Get the 'pretty name' of a job, i.e. either its 'name' (if defined) or the 'location' (URL or command).

        :returns: A string with the 'pretty name' the job.
        """
        return self.name or self.get_location()

    def retrieve(self, job_state: JobState, headless: bool = True) -> Tuple[Union[str, bytes], str]:
        """Runs job to retrieve the data, and returns data and ETag.

        :param job_state: The JobState object, to keep track of the state of the retrieval.
        :param headless: For browser-based jobs, whether headless mode should be used.
        :returns: The data retrieved and the ETag.
        """
        pass


CHARSET_RE = re.compile('text/(html|plain); charset=([^;]*)')


class UrlJobBase(Job):
    """The base class for jobs that use the 'url' key."""

    __required__: Tuple[str, ...] = ('url',)
    __optional__: Tuple[str, ...] = (
        'ignore_connection_errors',
        'ignore_http_error_codes',
        'ignore_timeout_errors',
        'ignore_too_many_redirects',
    )


class UrlJob(UrlJobBase):
    """Retrieve a URL from a web server."""

    __kind__ = 'url'

    __required__ = ('url',)
    __optional__ = (
        'cookies',
        'data',
        'encoding',
        'headers',
        'http_proxy',
        'https_proxy',
        'ignore_cached',
        'ignore_dh_key_too_small',
        'method',
        'no_redirects',
        'ssl_no_verify',
        'timeout',
    )

    def get_location(self) -> str:
        """Get the 'location' of a job, i.e. the URL or command.

        :returns: A string with user_visible_url or the URL of the job.
        """
        return self.user_visible_url or self.url

    def retrieve(self, job_state: JobState, headless: bool = True) -> Tuple[Union[str, bytes], str]:
        """Runs job to retrieve the data, and returns data and ETag.

        :param job_state: The JobState object, to keep track of the state of the retrieval.
        :param headless: For browser-based jobs, whether headless mode should be used.
        :returns: The data retrieved and the ETag.
        :raises NotModifiedError: If an HTTP 304 response is received.
        """
        if self._delay:
            logger.debug(f'Delaying for {self._delay} seconds (duplicate network location)')
            time.sleep(self._delay)

        headers: CaseInsensitiveDict = CaseInsensitiveDict(getattr(self, 'headers', {}))
        if 'User-Agent' not in headers:
            headers['User-Agent'] = __user_agent__

        proxies = {
            'http': os.getenv('HTTP_PROXY'),
            'https': os.getenv('HTTPS_PROXY'),
        }

        if job_state.old_etag:
            # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag#caching_of_unchanged_resources
            headers['If-None-Match'] = job_state.old_etag

        if job_state.old_timestamp is not None:
            headers['If-Modified-Since'] = email.utils.formatdate(job_state.old_timestamp)

        if self.ignore_cached or job_state.tries > 0:
            headers.pop('If-None-Match', None)
            headers['If-Modified-Since'] = email.utils.formatdate(0)
            headers['Cache-Control'] = 'max-age=172800'
            headers['Expires'] = email.utils.formatdate()

        if self.data is not None:
            if self.method is None:
                self.method = 'POST'
            if 'Content-Type' not in headers:
                headers['Content-Type'] = 'application/x-www-form-urlencoded'
            if isinstance(self.data, dict):
                self.data = urlencode(self.data)
            logger.info(f'Job {self.index_number}: Sending POST request to {self.url}')

        if self.method is None:
            self.method = 'GET'

        if self.http_proxy is not None:
            proxies['http'] = self.http_proxy
        if self.https_proxy is not None:
            proxies['https'] = self.https_proxy

        if urlparse(self.url).scheme == 'file':
            logger.info(f'Job {self.index_number}: Using local filesystem (file URI scheme)')

            if os.name == 'nt':
                filename = Path(str(urlparse(self.url).path).lstrip('/'))
            else:
                filename = Path(str(urlparse(self.url).path))

            if FilterBase.filter_chain_needs_bytes(self.filter):
                return filename.read_bytes(), ''
            else:
                return filename.read_text(), ''

        if urlparse(self.url).scheme == 'ftp':
            url = urlparse(self.url)
            username = url.username or 'anonymous'
            password = url.password or 'anonymous'

            with FTP(
                str(url.hostname),
                str(username),
                str(password),
                timeout=self.timeout,  # type: ignore[arg-type]
            ) as ftp:  # nosec: B321
                if FilterBase.filter_chain_needs_bytes(self.filter):
                    data_bytes = b''

                    def callback_bytes(dt: bytes) -> None:
                        """Handle FTP callback."""
                        nonlocal data_bytes
                        data_bytes += dt

                    ftp.retrbinary(f'RETR {url.path}', callback_bytes)

                    return data_bytes, ''
                else:
                    data: List[str] = []

                    def callback(dt: str) -> None:
                        """Handle FTP callback."""
                        data.append(dt)

                    ftp.retrlines(f'RETR {url.path}', callback)

                    return '\n'.join(data), ''

        # if self.headers:
        #     self.add_custom_headers(headers)

        if self.timeout is None:
            # default timeout
            timeout: Optional[float] = 60.0
        elif self.timeout == 0:
            # never timeout
            timeout = None
        else:
            timeout = self.timeout

        # cookiejar (called by requests) expects strings or bytes-like objects; PyYAML will try to guess int etc.
        if self.cookies:
            self.cookies = {k: str(v) for k, v in self.cookies.items()}

        if self.ignore_dh_key_too_small:
            # https://stackoverflow.com/questions/38015537
            logger.debug(
                'Setting default cipher list to ciphers that do not make any use of Diffie Hellman Key Exchange and '
                "thus not affected by the server's weak DH key"
            )
            requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'  # type: ignore[attr-defined]

        response = requests.request(
            method=self.method,
            url=self.url,
            data=self.data,
            headers=headers,
            cookies=self.cookies,
            timeout=timeout,
            allow_redirects=(not self.no_redirects),
            proxies=proxies,
            verify=(not self.ssl_no_verify),
        )

        if 400 <= response.status_code <= 499:
            logger.info(
                f'Job {self.index_number}: Received HTTP status code {response.status_code} ({response.reason}) with'
                f' the following content:'
            )
            error_message = response.text
            try:
                parsed_json = json.loads(error_message)
                error_message = json.dumps(parsed_json, ensure_ascii=False, separators=(',', ': '))
            except json.decoder.JSONDecodeError:
                error_message = html2text.HTML2Text().handle(error_message).strip()
            logger.info(error_message)

        response.raise_for_status()
        if response.status_code == requests.codes.not_modified:
            raise NotModifiedError(response.status_code)

        # Save ETag from response into job_state, saved in cache and used in future requests in If-None-Match header
        etag = ''
        if not response.history:  # no redirects
            etag = response.headers.get('ETag', '')

        if FilterBase.filter_chain_needs_bytes(self.filter):
            return response.content, etag

        if self.encoding:
            response.encoding = self.encoding
        elif response.encoding == 'ISO-8859-1' and not CHARSET_RE.match(response.headers.get('Content-type', '')):
            # requests follows RFC 2616 and defaults to ISO-8859-1 if no explicit charset is present in the HTTP headers
            # and the Content-Type header contains text, but this IRL is often wrong; the below updates it with
            # whatever response detects it to be by its use of the chardet library
            logger.debug(
                f'Job {self.index_number}: Encoding updated to {response.apparent_encoding} from '
                f'{response.encoding}'
            )
            response.encoding = response.apparent_encoding

        # if no name directive is given, set it to the title element if found in HTML or XML truncated to 60 characters
        if not self.name:
            title = re.search(r'<title.*?>(.+?)</title>', response.text)
            if title:
                self.name = html.unescape(title.group(1))[:60]

        return response.text, etag

    # def add_custom_headers(self, headers: Dict[str, Any]) -> None:
    #     """
    #     Adds custom request headers from the job list (URLs) to the pre-filled dictionary `headers`.
    #     Pre-filled values of conflicting header keys (case-insensitive) are overwritten by custom value.
    #     """
    #     headers_to_remove = [x for x in headers if x.lower() in (y.lower() for y in self.headers)]
    #     for header in headers_to_remove:
    #         headers.pop(header, None)
    #     headers.update(self.headers)

    def format_error(self, exception: Exception, tb: str) -> str:
        """Format the error of the job if one is encountered.

        :param exception: The exception.
        :param tb: The traceback.
        :returns: A string to display and/or use in reports.
        """
        if isinstance(exception, requests.exceptions.RequestException):
            # Instead of a full traceback, just show the HTTP error
            return str(exception)
        return tb

    def ignore_error(self, exception: Exception) -> bool:
        """Determine whether the error of the job should be ignored.

        :param exception: The exception.
        :returns: True if the error should be ignored, False otherwise.
        """
        if isinstance(exception, requests.exceptions.ConnectionError) and self.ignore_connection_errors:
            return True
        if isinstance(exception, requests.exceptions.Timeout) and self.ignore_timeout_errors:
            return True
        if isinstance(exception, requests.exceptions.TooManyRedirects) and self.ignore_too_many_redirects:
            return True
        elif isinstance(exception, requests.exceptions.HTTPError) and self.ignore_http_error_codes:
            status_code = exception.response.status_code
            ignored_codes: List[str] = []
            if isinstance(self.ignore_http_error_codes, int) and self.ignore_http_error_codes == status_code:
                return True
            elif isinstance(self.ignore_http_error_codes, str):
                ignored_codes = [s.strip().lower() for s in self.ignore_http_error_codes.split(',')]
            elif isinstance(self.ignore_http_error_codes, list):
                ignored_codes = [str(s).strip().lower() for s in self.ignore_http_error_codes]
            return str(status_code) in ignored_codes or f'{(status_code // 100)}xx' in ignored_codes
        return False


class BrowserJob(UrlJobBase):
    """Retrieve a URL, emulating a real web browser (use_browser: true)."""

    __kind__ = 'browser'

    __required__ = ('url', 'use_browser')
    __optional__ = (
        '_beta_use_playwright',
        'block_elements',
        'chromium_revision',
        'cookies',
        'data',
        'headers',
        'http_proxy',
        'https_proxy',
        'ignore_https_errors',
        'initialization_js',  # Playwright
        'initialization_url',  # Playwright  # TODO documentation
        'method',
        'navigate',
        'switches',
        'timeout',
        'user_data_dir',
        'wait_for',  # pyppeteer
        'wait_for_function',  # Playwright
        'wait_for_navigation',  # pyppeteer
        'wait_for_selector',  # Playwright
        'wait_for_url',
        'wait_until',
    )

    _playwright: Optional[Any] = None
    _playwright_browsers: dict = {}

    proxy_username: str = ''
    proxy_password: str = ''

    def get_location(self) -> str:
        """Get the 'location' of a job, i.e. the URL or command.

        :returns: A string with user_visible_url or the URL of the job.
        """
        return self.user_visible_url or self.url

    def retrieve(self, job_state: JobState, headless: bool = True) -> Tuple[Union[str, bytes], str]:
        """Runs job to retrieve the data, and returns data and ETag.

        :param job_state: The JobState object, to keep track of the state of the retrieval.
        :param headless: For browser-based jobs, whether headless mode should be used.
        :returns: The data retrieved and the ETag.
        """
        if self._delay:
            logger.debug(f'Delaying for {self._delay} seconds (duplicate network location)')
            time.sleep(self._delay)

        if self._beta_use_playwright:
            response, etag = self._playwright_retrieve(job_state, headless)
        else:
            response, etag = asyncio.run(self._retrieve(job_state))  # pragma: no cover

        # if no name directive is given, set it to the title element if found in HTML or XML truncated to 60 characters
        if not self.name:
            title = re.findall(r'<title.*?>(.+?)</title>', response)
            if title:
                self.name = html.unescape(title[0])[:60]

        return response, etag

    @staticmethod
    def current_platform() -> str:  # pragma: no cover
        """Get current platform name by short string as used by Pyppeteer for downloading Chromium.
        Code originally from pyppeteer.chromium_downloader, but we cannot simply import it as it will trigger
        pyppeteer reading os.environ['PYPPETEER_CHROMIUM_REVISION'] before we can modify it ourselves.

        :raises OSError: If the platform is not supported by Pyppeteer.
        """
        if sys.platform.startswith('linux'):
            return 'linux'
        elif sys.platform.startswith('darwin'):
            return 'mac'
        elif sys.platform.startswith('win') or sys.platform.startswith('msys') or sys.platform.startswith('cyg'):
            if sys.maxsize > 2 ** 31 - 1:
                return 'win64'
            return 'win32'
        raise OSError(f'Platform unsupported by Pyppeteer (use_browser: true): {sys.platform}')

    async def _retrieve(self, job_state: JobState) -> Tuple[str, str]:  # pragma: no cover
        """

        :raises KeyError: If chromium_revision is specified but not for the current operating system.
        :raises ValueError: If there is a problem with the value supplied in one of the keys in the configuration file.
        :raises TypeError: If the value provided in one of the directives is not in the correct type.
        :raises ImportError: If the pyppeteer package is not installed.
        :raises BrowserResponseError: If an HTTP response code between 400 and 599 is received.
        :raises PageError: If another response code or error is received.
        """
        # launch browser
        if not self.chromium_revision:
            self.chromium_revision = DEFAULT_CHROMIUM_REVISION
        if isinstance(self.chromium_revision, dict):
            for key, value in DEFAULT_CHROMIUM_REVISION.items():
                if key not in self.chromium_revision:
                    self.chromium_revision[key] = value  # type: ignore[assignment]
            try:
                _revision: Union[str, int] = self.chromium_revision[self.current_platform()]
            except KeyError:
                raise KeyError(f"No 'chromium_revision' key for operating system {self.current_platform()} found")
        else:
            _revision = self.chromium_revision
        os.environ['PYPPETEER_CHROMIUM_REVISION'] = str(_revision)

        logger.info(
            f'Job {self.index_number}: '
            f"PYPPETEER_CHROMIUM_REVISION={os.environ.get('PYPPETEER_CHROMIUM_REVISION')}, "
            f"PYPPETEER_NO_PROGRESS_BAR={os.environ.get('PYPPETEER_NO_PROGRESS_BAR')}, "
            f"PYPPETEER_DOWNLOAD_HOST={os.environ.get('PYPPETEER_DOWNLOAD_HOST')}"
        )
        try:
            from pyppeteer import launch  # pyppeteer must be imported after setting os.environ variables
        except ImportError:
            raise ImportError(
                f'Job {job_state.job.index_number}: Python package pyppeteer is not installed; cannot use the '
                f"'use_browser: true' directive ( {self.get_indexed_location()} )"
            )
        import pyppeteer.network_manager
        from pyppeteer.errors import PageError

        # Setting of 'If-None-Match' or 'If-Modified-Since' headers can trigger a 'net::ERR_ABORTED [...]'
        # browsing error that is returned by page.goto as a PageError(); cannot find a workable way to determine whether
        # it's due to an HTTP 304 Not Modified code (goto) or something else (bad) as PageError only passes the text,
        # not the full response. Keeping code here for future ETag handling development.
        # if self.ignore_cached or job_state.tries > 0:
        #     headers.pop('If-None-Match', None)
        #     headers['If-Modified-Since'] = email.utils.formatdate(0)
        #     headers['Cache-Control'] = 'max-age=172800'
        #     headers['Expires'] = email.utils.formatdate()
        # else:
        #     if job_state.old_etag:
        #         # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag#caching_of_unchanged_resources
        #         headers['If-None-Match'] = job_state.old_etag
        #     if job_state.old_timestamp is not None:
        #         headers['If-Modified-Since'] = email.utils.formatdate(job_state.old_timestamp)

        args: List[str] = []
        proxy: Optional[str] = ''
        if self.http_proxy or self.https_proxy:
            if urlsplit(self.url).scheme == 'http':
                proxy = self.http_proxy
            elif urlsplit(self.url).scheme == 'https':
                proxy = self.https_proxy
            if proxy:
                proxy_server = f'{urlsplit(proxy).scheme}://{urlsplit(proxy).hostname}' + (
                    f':{urlsplit(proxy).port}' if urlsplit(proxy).port else ''
                )
                args.append(f'--proxy-server={proxy_server}')

        if self.user_data_dir:
            args.append(f'--user-data-dir={self.user_data_dir}')

        if self.switches:
            if isinstance(self.switches, str):
                self.switches = self.switches.split(',')
            if not isinstance(self.switches, list):
                raise TypeError(
                    f"Job {job_state.job.index_number}: Directive 'switches' needs to be a string or list, not"
                    f' {type(self.switches)} ( {self.get_indexed_location()} )'
                )
            self.switches = [f"--{switch.lstrip('--')}" for switch in self.switches]
            args.extend(self.switches)

        logger.debug(f'Job {self.index_number}: About to launch browser with args={args}')
        browser = await launch(
            ignoreHTTPSErrors=self.ignore_https_errors,
            args=args,
            handleSIGINT=False,
            handleSIGTERM=False,
            handleSIGHUP=False,
            loop=asyncio.get_running_loop(),
        )  # as signals only work single-threaded, must set handleSIGINT, handleSIGTERM and handleSIGHUP to False
        logger.debug(f'Job {self.index_number}: Browser launched')

        # browse to page and get content
        page = await browser.newPage()

        headers: CaseInsensitiveDict = CaseInsensitiveDict(getattr(self, 'headers', {}))
        if 'User-Agent' not in headers:
            headers['User-Agent'] = __user_agent__

        if self.data is not None:
            if self.method is None:
                self.method = 'POST'
            if 'Content-Type' not in headers:
                headers['Content-Type'] = 'application/x-www-form-urlencoded'
            if isinstance(self.data, dict):
                self.data = urlencode(self.data)
            logger.info(f'Job {self.index_number}: Sending POST request to {self.url}')

        if headers:
            logger.debug(f'Job {self.index_number}: setExtraHTTPHeaders={headers}')
            await page.setExtraHTTPHeaders(dict(headers))

        if self.cookies:
            await page.setExtraHTTPHeaders({'Cookies': '; '.join([f'{k}={v}' for k, v in self.cookies.items()])})

        if self.http_proxy or self.https_proxy:
            proxy_username = urlsplit(proxy).username if urlsplit(proxy).username else ''
            proxy_password = urlsplit(proxy).password if urlsplit(proxy).password else ''
            if proxy_username or proxy_password:
                await page.authenticate({'username': proxy_username, 'password': proxy_password})
                logger.debug(
                    f'Job {self.index_number}: Set page.authenticate with '  # type: ignore[str-bytes-safe]
                    f'username={proxy_username}, password={proxy_password}'
                )
        options: Dict[str, Any] = {}

        if self.timeout:
            options['timeout'] = self.timeout * 1000

        if self.wait_until:
            options['waitUntil'] = self.wait_until

        if self.method and self.method != 'GET':

            async def post_intercept(request_event: pyppeteer.network_manager.Request) -> None:
                """Handle pyee.EventEmitter callback."""
                logger.info(
                    f'Job {self.index_number}: Intercepted request with resource_type'
                    f'={request_event.resourceType}; overriding request method to {self.method}'
                )
                await request_event.continue_(overrides={'method': self.method, 'postData': self.data})

            await page.setRequestInterception(True)
            page.on(
                'request', lambda request_event: asyncio.create_task(post_intercept(request_event))
            )  # inherited from pyee.EventEmitter

        if self.block_elements and not self.method or self.method == 'GET':
            # FIXME: Pyppeteer freezes on certain sites if this is on; contribute if you know why
            if isinstance(self.block_elements, str):
                self.block_elements = self.block_elements.split(',')
            if not isinstance(self.block_elements, list):
                await browser.close()
                raise TypeError(
                    f"Job {job_state.job.index_number}: Directive 'block_elements' needs to be a string or list, not"
                    f' {type(self.block_elements)} ( {self.get_indexed_location()} )'
                )
            chrome_web_request_resource_types = [
                'main_frame',
                'sub_frame',
                'stylesheet',
                'script',
                'image',
                'font',
                'object',
                'xmlhttprequest',
                'ping',
                'csp_report',
                'media',
                'websocket',
                'other',
            ]  # https://developer.chrome.com/docs/extensions/reference/webRequest/#type-ResourceType
            for element in self.block_elements:
                if element not in chrome_web_request_resource_types:
                    await browser.close()
                    raise ValueError(
                        f"Job {job_state.job.index_number}: Unknown or unsupported '{element}' resource type in"
                        f" 'block_elements' ( {self.get_indexed_location()} )"
                    )

            async def handle_request(
                request_event: pyppeteer.network_manager.Request, block_elements: List[str]
            ) -> None:
                """Handle pyee.EventEmitter callback."""
                logger.info(
                    f'Job {self.index_number}: resource_type={request_event.resourceType} elements={block_elements}'
                )
                if any(request_event.resourceType == el for el in block_elements):
                    logger.info(f'Job {self.index_number}: Aborting request {request_event.resourceType}')
                    await request_event.abort()
                else:
                    logger.info(f'Job {self.index_number}: Continuing request {request_event.resourceType}')
                    await request_event.continue_()  # broken -- many sites hang here!

            await page.setRequestInterception(True)
            page.on(
                'request', lambda request_event: asyncio.create_task(handle_request(request_event, self.block_elements))
            )  # inherited from pyee.EventEmitter

        async def store_etag(response_event: pyppeteer.network_manager.Response) -> None:
            """Store the ETag for future use as well as the response code."""
            nonlocal etag  # type: ignore[misc]
            nonlocal response_code  # type: ignore[misc]
            nonlocal response_headers  # type: ignore[misc]
            logger.debug(
                f'Job {self.index_number}: response.status={response_event.status} '
                f'response.url={response_event.url}'
            )
            if urldefrag(response_event.url)[0] == urldefrag(self.url)[0]:
                response_code = response_event.status
                response_headers = response_event.headers
                if response_event.status == requests.codes.ok:
                    etag = response_event.headers.get('etag')

        etag: str = ''
        response_code: Optional[int] = None
        response_headers: Optional[Dict[str, str]] = {}

        # page.on inherited from pyee's EventEmitter class
        # https://pyee.readthedocs.io/en/latest/#pyee.EventEmitter
        page.on('response', lambda response_event: asyncio.create_task(store_etag(response_event)))

        try:
            logger.debug(f'Job {self.index_number}: page.goto options={options}')
            await page.goto(self.url, options=options)
        except PageError as e:
            logger.debug(f'Job {self.index_number}: Page returned error {str(e.args)}')
            logger.debug(f'Job {self.index_number}: Response headers {response_headers}')
            await browser.close()
            if response_code and 400 <= response_code < 600:
                raise BrowserResponseError(e.args, response_code)
            else:
                raise PageError(e)

        # For future ETag handling development, the code in remarks below triggers NotModifiedError if HTTP 304 Not
        # Modified is returned
        # page_response = await page.goto(self.url, options=options)
        # if not request_response and response_code == requests.codes.not_modified:
        #     logger.debug(f'Job {self.index_number}: page_response={page_response}; response_code={response_code}')
        #     await browser.close()
        #     raise NotModifiedError(response_code)

        if self.wait_for_navigation:
            while not page.url.startswith(self.wait_for_navigation):
                logger.info(f'Job {self.index_number}: Waiting for redirection from {page.url}')
                logger.debug(f'Job {self.index_number}: Response headers {response_headers}')
                await page.waitForNavigation(option=options)
        if self.wait_for:
            if isinstance(self.wait_for, (int, float, complex)) and not isinstance(self.wait_for, bool):
                self.wait_for *= 1000
            await page.waitFor(self.wait_for, options=options)

        content = await page.content()
        await browser.close()

        if response_code and 400 <= response_code < 600:
            raise BrowserResponseError(('',), response_code)
        elif response_code is not None and response_code != requests.codes.ok:
            logger.info(
                f'Job {self.index_number}: Received response HTTP {response_code} {response_names[response_code]}'
            )
            logger.debug(f'Job {self.index_number}: Response headers {response_headers}')

        return content, etag

    def _playwright_retrieve(self, job_state: JobState, headless: bool = True) -> Tuple[str, str]:
        """

        :raises ValueError: If there is a problem with the value supplied in one of the keys in the configuration file.
        :raises TypeError: If the value provided in one of the directives is not of the correct type.
        :raises ImportError: If the playwright package is not installed.
        :raises BrowserResponseError: If a browser error or an HTTP response code between 400 and 599 is received.
        """
        try:
            from playwright.sync_api import Error as PlaywrightError
            from playwright.sync_api import Route, sync_playwright
        except ImportError:
            raise ImportError(
                f'Job {job_state.job.index_number}: Python package playwright is not installed; cannot use the '
                f'"use_browser: true" directive ( {self.get_indexed_location()} )'
            )

        # deprecations
        if self.wait_until in ('networkidle0', 'networkidle2'):
            self.wait_until = 'networkidle'  # type: ignore[assignment]  # pyppeteer Literal
        if self.wait_for_navigation:
            warnings.warn(
                f"Job {self.index_number}: Directive 'wait_for_navigation' is deprecated with Playwright; "
                "for future compatibility replace it with 'wait_for_url'.",
                DeprecationWarning,
            )
            self.wait_for_url = self.wait_for_navigation  # type: ignore[assignment]
        if self.wait_for:
            raise ValueError(
                f"Job {job_state.job.index_number}: Directive 'wait_for' is deprecated with Playwright; replace with "
                f"'wait_for_selector' or 'wait_for_function'."
            )

        headers: CaseInsensitiveDict = CaseInsensitiveDict(getattr(self, 'headers', {}))
        if self.ignore_cached or job_state.tries > 0:
            headers.pop('If-None-Match', None)
            headers['If-Modified-Since'] = email.utils.formatdate(0)
            headers['Cache-Control'] = 'max-age=172800'
            headers['Expires'] = email.utils.formatdate()
        else:
            if job_state.old_etag:
                # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag#caching_of_unchanged_resources
                headers['If-None-Match'] = job_state.old_etag
            if job_state.old_timestamp is not None:
                headers['If-Modified-Since'] = email.utils.formatdate(job_state.old_timestamp)
        if self.cookies:
            headers['Cookies'] = '; '.join([f'{k}={quote(v)}' for k, v in self.cookies.items()])

        data = None
        if self.data:
            if not self.method:
                self.method = 'POST'
            if 'Content-Type' not in headers:
                headers['Content-Type'] = 'application/x-www-form-urlencoded'
            logger.info(f'Job {self.index_number}: Sending POST request to {self.url}')
            if isinstance(self.data, dict):
                data = urlencode(self.data)
            else:
                data = quote(self.data)

        proxy = None
        if self.http_proxy or self.https_proxy:
            if urlsplit(self.url).scheme == 'http':
                proxy_split: Optional[Union[SplitResult, SplitResultBytes]] = urlsplit(self.http_proxy)
            elif urlsplit(self.url).scheme == 'https':
                proxy_split = urlsplit(self.https_proxy)
            else:
                proxy_split = None
            if proxy_split:
                proxy = {
                    'server': f'{proxy_split.scheme!s}://{proxy_split.hostname!s}:{proxy_split.port!s}'
                    if proxy_split.port
                    else '',
                    'username': proxy_split.username,
                    'password': proxy_split.password,
                }

        if self.switches:
            if isinstance(self.switches, str):
                self.switches = self.switches.split(',')
            if not isinstance(self.switches, list):
                raise TypeError(
                    f"Job {job_state.job.index_number}: Directive 'switches' needs to be a string or list, not"
                    f' {type(self.switches)} ( {self.get_indexed_location()} )'
                )
            args: Optional[List[str]] = [f"--{switch.lstrip('--')}" for switch in self.switches]
        else:
            args = None

        timeout = self.timeout * 1000 if self.timeout else 75000  # Browser could be slow to launch

        # launch browser
        with sync_playwright() as p:
            executable_path = os.getenv('WEBCHANGES_BROWSER_PATH')
            channel = None if executable_path else 'chrome'
            no_viewport = False if not self.switches else any('--window-size' in switch for switch in self.switches)
            if not self.user_data_dir:
                browser = p.chromium.launch(
                    executable_path=executable_path,  # type: ignore[arg-type]
                    channel=channel,  # type: ignore[arg-type]
                    args=args,  # type: ignore[arg-type]
                    timeout=timeout,  # type: ignore[arg-type]
                    headless=headless,  # type: ignore[arg-type]
                    proxy=proxy,  # type: ignore[arg-type]
                )
                if 'User-Agent' not in headers:
                    headers['User-Agent'] = (
                        f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        f'Chrome/{browser.version} Safari/537.36'
                    )
                context = browser.new_context(
                    no_viewport=no_viewport,
                    ignore_https_errors=self.ignore_https_errors,  # type: ignore[arg-type]
                    extra_http_headers=dict(headers),
                )
                logger.debug(
                    f'Job {self.index_number}: Launched browser {channel or executable_path} version {browser.version}'
                )
            else:
                context = p.chromium.launch_persistent_context(
                    user_data_dir=self.user_data_dir,
                    channel=channel,  # type: ignore[arg-type]
                    executable_path=executable_path,  # type: ignore[arg-type]
                    args=args,  # type: ignore[arg-type]
                    # handle_sigint=False,
                    # handle_sigterm=False,
                    # handle_sighup=False,
                    timeout=timeout,  # type: ignore[arg-type]
                    headless=headless,
                    proxy=proxy,  # type: ignore[arg-type]
                    no_viewport=no_viewport,
                    ignore_https_errors=self.ignore_https_errors,  # type: ignore[arg-type]
                    extra_http_headers=dict(headers),
                )
                logger.debug(
                    f'Job {self.index_number}: Launched browser {channel or executable_path} version'
                    f' {context.browser.version} with user data directory '  # type: ignore[union-attr]
                    f'{self.user_data_dir}'
                )

            # # launch playwright (memoized)
            # if self._playwright is None:
            #     logger.info('Starting the instance of playwright')
            #     self._playwright = sync_playwright().start()  # TODO this should be in a context manager with .stop()

            # # launch browser (memoized)
            # executable_path = os.getenv('WEBCHANGES_BROWSER_PATH')
            # browser_key = msgpack.packb({1: executable_path, 2: args, 3: self.headless})
            # browser = self._playwright_browsers.get(browser_key)
            # print(f'playwright about to start browser for job {job_state.job.index_number}')
            # if not browser:
            #     logger.info(f'Starting a new browser with key {browser_key}')
            #     print(f'Starting a new browser with key {browser_key}')
            #     channel = None if executable_path else 'chrome'
            #     playwright = job_state.playwright
            #     if not playwright:
            #         print(f'No playwright found for job {job_state.job.index_number}')
            #         playwright = sync_playwright().start()
            #     browser = playwright.chromium.launch(
            #         executable_path=executable_path,
            #         channel=channel,
            #         args=args,
            #         headless=self.headless,
            #         proxy={'server': 'http://per-context'},
            #     )
            #     print(f'playwright browser launched for job {job_state.job.index_number}')
            #     self._playwright_browsers[browser_key] = browser
            #
            # # launch new browser context for this job
            #
            # context = browser.new_context(
            #     ignore_https_errors=self.ignore_https_errors,
            #     extra_http_headers=dict(headers),
            #     proxy=proxy,
            # )

            # open a page
            page = context.new_page()

            if self.initialization_url:
                logger.info(f'Job {self.index_number}: Initializing website by navigating to {self.initialization_url}')
                try:
                    response = page.goto(
                        self.initialization_url,
                        timeout=timeout,
                    )
                except PlaywrightError as e:
                    context.close()
                    logger.error(f'Job {self.index_number}: Website initialization page returned error' f' {e.args[0]}')
                    raise e

                if not response:
                    context.close()
                    raise BrowserResponseError(('No response received from browser',), None)

                if self.initialization_js:
                    logger.info(f'Job {self.index_number}: Running init script {self.initialization_js}')
                    page.evaluate(self.initialization_js)
                    if self.wait_for_url:
                        logger.info(f'Job {self.index_number}: Waiting for url {self.wait_for_url}')
                        response.frame.wait_for_url(
                            self.wait_for_url, wait_until=self.wait_until, timeout=timeout  # type: ignore[arg-type]
                        )
                updated_url = page.url
                params = dict(parse_qsl(urlparse(updated_url).params))
                try:
                    new_url = self.url.format(**params)
                except KeyError as e:
                    browser.close()
                    raise ValueError(
                        f"Job {job_state.job.index_number}: Directive 'initialization_url' did not find key"
                        f" {e.args[0]} to substitute in 'url'"
                    )
                if new_url != self.url:
                    self.url = new_url
                    logger.info(f'Job {self.index_number}: URL updated to {self.url}')

            if self.method and self.method != 'GET':

                def handle_route(route: Route) -> None:
                    """Handler function to change the route (a pyee.EventEmitter callback)."""
                    logger.info(f'Job {self.index_number}: Intercepted route to change request method to {self.method}')
                    route.continue_(method=str(self.method), post_data=data)  # type: ignore[arg-type]

                page.route(self.url, handler=handle_route)

            # if self.block_elements and not self.method or self.method == 'GET':
            #     # FIXME: Pyppeteer freezes on certain sites if this is on; contribute if you know why
            #     if isinstance(self.block_elements, str):
            #         self.block_elements = self.block_elements.split(',')
            #     if not isinstance(self.block_elements, list):
            #         browser.close()
            #         raise TypeError(
            #             f"'block_elements' needs to be a string or list, not {type(self.block_elements)} "
            #             f'( {self.get_indexed_location()} )'
            #         )
            #     chrome_web_request_resource_types = [
            #         'main_frame',
            #         'sub_frame',
            #         'stylesheet',
            #         'script',
            #         'image',
            #         'font',
            #         'object',
            #         'xmlhttprequest',
            #         'ping',
            #         'csp_report',
            #         'media',
            #         'websocket',
            #         'other',
            #     ]  # https://developer.chrome.com/docs/extensions/reference/webRequest/#type-ResourceType
            #     for element in self.block_elements:
            #         if element not in chrome_web_request_resource_types:
            #             browser.close()
            #             raise ValueError(
            #                 f"Unknown or unsupported '{element}' resource type in 'block_elements' "
            #                 f'( {self.get_indexed_location()} )'
            #             )
            #
            #     def handle_request(
            #         request_event: pyppeteer.network_manager.Request, block_elements: List[str]
            #     ) -> None:
            #         """Handle pyee.EventEmitter callback."""
            #         logger.info(
            #             f'Job {self.index_number}: resource_type={request_event.resourceType}'
            #             f' elements={block_elements}'
            #         )
            #         if any(request_event.resourceType == el for el in block_elements):
            #             logger.info(f'Job {self.index_number}: Aborting request {request_event.resourceType}')
            #             request_event.abort()
            #         else:
            #             logger.info(
            #                 f'Job {self.index_number}: Continuing request {request_event.resourceType}'
            #             )
            #             request_event.continue_()  # broken -- many sites hang here!
            #
            #     page.setRequestInterception(True)
            #     page.on(
            #         'request',
            #         lambda request_event: asyncio.create_task(
            #              handle_request(request_event, self.block_elements)
            #          ),
            #     )  # inherited from pyee.EventEmitter

            # navigate page
            logger.debug(f'Job {self.index_number}: Navigating to {self.url} with headers {headers}')
            try:
                response = page.goto(
                    self.url,
                    wait_until=self.wait_until,  # type: ignore[arg-type]
                    referer=self.referer,  # type: ignore[arg-type]
                    timeout=timeout,
                )
            except PlaywrightError as e:
                logger.error(f'Job {self.index_number}: Page returned error {e.args[0]}')
                context.close()
                raise BrowserResponseError(e.args, None)

            if not response:
                context.close()
                raise BrowserResponseError(('No response received from browser',), None)

            # wait_for-*
            if self.wait_for_url:
                response.frame.wait_for_url(
                    self.wait_for_url, wait_until=self.wait_until, timeout=timeout  # type: ignore[arg-type]
                )
            if self.wait_for_selector:
                if isinstance(self.wait_for_selector, str):
                    response.frame.wait_for_selector(self.wait_for_selector, timeout=timeout)
                elif isinstance(self.wait_for_selector, dict):
                    response.frame.wait_for_selector(**self.wait_for_selector, timeout=timeout)
                else:
                    context.close()
                    raise ValueError(
                        f"Job {job_state.job.index_number}: Directive 'wait_for_selector' can only be a string or a"
                        f' dictionary; found {type(self.wait_for_selector)}.'
                    )
            if self.wait_for_function:
                if isinstance(self.wait_for_function, str):
                    response.frame.wait_for_function(self.wait_for_function, timeout=timeout)

                elif isinstance(self.wait_for_function, dict):
                    response.frame.wait_for_function(**self.wait_for_function, timeout=timeout)
                else:
                    context.close()
                    raise ValueError(
                        f"Job {job_state.job.index_number}: Directive 'wait_for_function' can only be a string or a"
                        f' dictionary; found {type(self.wait_for_function)}'
                    )

            # if response.status and 400 <= response.status < 600:
            #     raise BrowserResponseError((response.status_text,), response.status)
            if not response.ok:
                # logger.info(
                #     f'Job {self.index_number}: Received response HTTP {response.status} {response.status_text} from '
                #     f'{response.url}'
                # )
                # logger.debug(f'Job {self.index_number}: Response headers {response.all_headers()}')
                context.close()
                raise BrowserResponseError((response.status_text,), response.status)

            # extract content
            content = page.content()
            etag = response.header_value('etag') or ''
            context.close()
            return content, etag

    def ignore_error(self, exception: Exception) -> Union[bool, str]:
        """Determine whether the error of the job should be ignored.

        :param exception: The exception.
        :returns: True or the string with the number of the HTTPError code if the error should be ignored,
           False otherwise.
        """
        # See https://source.chromium.org/chromium/chromium/src/+/master:net/base/net_error_list.h
        CHROMIUM_CONNECTION_ERRORS = [  # range 100-199 Connection related errors
            'CONNECTION_CLOSED',
            'CONNECTION_RESET',
            'CONNECTION_REFUSED',
            'CONNECTION_ABORTED',
            'CONNECTION_FAILED',
            'NAME_NOT_RESOLVED',
            'INTERNET_DISCONNECTED',
            'SSL_PROTOCOL_ERROR',
            'ADDRESS_INVALID',
            'ADDRESS_UNREACHABLE',
            'SSL_CLIENT_AUTH_CERT_NEEDED',
            'TUNNEL_CONNECTION_FAILED',
            'NO_SSL_VERSIONS_ENABLED',
            'SSL_VERSION_OR_CIPHER_MISMATCH',
            'SSL_RENEGOTIATION_REQUESTED',
            'PROXY_AUTH_UNSUPPORTED',
            'CERT_ERROR_IN_SSL_RENEGOTIATION',
            'BAD_SSL_CLIENT_AUTH_CERT',
            'CONNECTION_TIMED_OUT',
            'HOST_RESOLVER_QUEUE_TOO_LARGE',
            'SOCKS_CONNECTION_FAILED',
            'SOCKS_CONNECTION_HOST_UNREACHABLE',
            'ALPN_NEGOTIATION_FAILED',
            'SSL_NO_RENEGOTIATION',
            'WINSOCK_UNEXPECTED_WRITTEN_BYTES',
            'SSL_DECOMPRESSION_FAILURE_ALERT',
            'SSL_BAD_RECORD_MAC_ALERT',
            'PROXY_AUTH_REQUESTED',
            'PROXY_CONNECTION_FAILED',
            'MANDATORY_PROXY_CONFIGURATION_FAILED',
            'PRECONNECT_MAX_SOCKET_LIMIT',
            'SSL_CLIENT_AUTH_PRIVATE_KEY_ACCESS_DENIED',
            'SSL_CLIENT_AUTH_CERT_NO_PRIVATE_KEY',
            'PROXY_CERTIFICATE_INVALID',
            'NAME_RESOLUTION_FAILED',
            'NETWORK_ACCESS_DENIED',
            'TEMPORARILY_THROTTLED',
            'HTTPS_PROXY_TUNNEL_RESPONSE_REDIRECT',
            'SSL_CLIENT_AUTH_SIGNATURE_FAILED',
            'MSG_TOO_BIG',
            'WS_PROTOCOL_ERROR',
            'ADDRESS_IN_USE',
            'SSL_HANDSHAKE_NOT_COMPLETED',
            'SSL_BAD_PEER_PUBLIC_KEY',
            'SSL_PINNED_KEY_NOT_IN_CERT_CHAIN',
            'CLIENT_AUTH_CERT_TYPE_UNSUPPORTED',
            'SSL_DECRYPT_ERROR_ALERT',
            'WS_THROTTLE_QUEUE_TOO_LARGE',
            'SSL_SERVER_CERT_CHANGED',
            'SSL_UNRECOGNIZED_NAME_ALERT',
            'SOCKET_SET_RECEIVE_BUFFER_SIZE_ERROR',
            'SOCKET_SET_SEND_BUFFER_SIZE_ERROR',
            'SOCKET_RECEIVE_BUFFER_SIZE_UNCHANGEABLE',
            'SOCKET_SEND_BUFFER_SIZE_UNCHANGEABLE',
            'SSL_CLIENT_AUTH_CERT_BAD_FORMAT',
            'ICANN_NAME_COLLISION',
            'SSL_SERVER_CERT_BAD_FORMAT',
            'CT_STH_PARSING_FAILED',
            'CT_STH_INCOMPLETE',
            'UNABLE_TO_REUSE_CONNECTION_FOR_PROXY_AUTH',
            'CT_CONSISTENCY_PROOF_PARSING_FAILED',
            'SSL_OBSOLETE_CIPHER',
            'WS_UPGRADE',
            'READ_IF_READY_NOT_IMPLEMENTED',
            'NO_BUFFER_SPACE',
            'SSL_CLIENT_AUTH_NO_COMMON_ALGORITHMS',
            'EARLY_DATA_REJECTED',
            'WRONG_VERSION_ON_EARLY_DATA',
            'TLS13_DOWNGRADE_DETECTED',
            'SSL_KEY_USAGE_INCOMPATIBLE',
            'INVALID_ECH_CONFIG_LIST',
        ]

        if self._beta_use_playwright:
            from playwright.async_api import Error as PlaywrightError
            from playwright.async_api import TimeoutError as PlaywrightTimeoutError

            if isinstance(exception, PlaywrightError):
                if self.ignore_connection_errors:
                    if isinstance(exception, PlaywrightTimeoutError) or any(
                        str(exception.args[0]).split()[0] == f'net::ERR_{error}' for error in CHROMIUM_CONNECTION_ERRORS
                    ):
                        return True
                if self.ignore_timeout_errors:
                    if (
                        isinstance(exception, PlaywrightTimeoutError)
                        or str(exception.args[0].split()[0]) == 'net::ERR_TIMED_OUT'
                    ):
                        return True
                if self.ignore_too_many_redirects:
                    if str(exception.args[0].split()[0]) == 'net::ERR_TOO_MANY_REDIRECTS':
                        return True

        else:
            from pyppeteer.errors import PageError  # pyppeteer must be imported after setting os.environ variables

            if isinstance(exception, PageError):
                if self.ignore_connection_errors:
                    if any(str(exception.args[0]) == f'net::ERR_{error}' for error in CHROMIUM_CONNECTION_ERRORS):
                        return True
                if self.ignore_timeout_errors:
                    if str(exception.args[0]) == 'net::ERR_TIMED_OUT':
                        return True
                if self.ignore_too_many_redirects:
                    if str(exception.args[0]) == 'net::ERR_TOO_MANY_REDIRECTS':
                        return True

        if isinstance(exception, BrowserResponseError) and self.ignore_http_error_codes:
            status_code = exception.status_code
            ignored_codes: List[str] = []
            if isinstance(self.ignore_http_error_codes, int) and self.ignore_http_error_codes == status_code:
                return True
            elif isinstance(self.ignore_http_error_codes, str):
                ignored_codes = [s.strip().lower() for s in self.ignore_http_error_codes.split(',')]
            elif isinstance(self.ignore_http_error_codes, list):
                ignored_codes = [str(s).strip().lower() for s in self.ignore_http_error_codes]
            if isinstance(status_code, int):
                return str(status_code) in ignored_codes or f'{(status_code // 100) in ignored_codes}xx'
            else:
                return str(status_code)
        return False


class ShellJob(Job):
    """Run a shell command and get its standard output."""

    __kind__ = 'shell'

    __required__ = ('command',)
    __optional__ = ('stderr',)  # ignored; here for backwards compatibility

    def get_location(self) -> str:
        """Get the 'location' of a job, i.e. the URL or command.

        :returns: A string with user_visible_url or the command of the job.
        """
        return self.user_visible_url or self.command

    def retrieve(self, job_state: JobState, headless: bool = True) -> Tuple[Union[str, bytes], str]:
        """Runs job to retrieve the data, and returns data and ETag (which is blank).

        :param job_state: The JobState object, to keep track of the state of the retrieval.
        :param headless: For browser-based jobs, whether headless mode should be used.
        :returns: The data retrieved and the ETag.
        :raises subprocess.CalledProcessError: Subclass of SubprocessError, raised when a process returns a non-zero
           exit status.
        :raises subprocess.TimeoutExpired: Subclass of SubprocessError, raised when a timeout expires while waiting for
           a child process.
        """
        needs_bytes = FilterBase.filter_chain_needs_bytes(self.filter)
        return (
            subprocess.run(self.command, capture_output=True, shell=True, check=True, text=(not needs_bytes)).stdout,
            '',
        )  # noqa: DUO116 use of "shell=True" is insecure
