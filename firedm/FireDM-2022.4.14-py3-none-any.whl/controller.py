"""
    FireDM

    multi-connections internet download manager, based on "LibCurl"

    :copyright: (c) 2019-2021 by Mahmoud Elshahat.
    :license: GNU LGPLv3, see LICENSE for more details.

    module description:
        This is the controller module as a part of MVC design, which will replace the old application design
        in attempt to isolate logic from gui / view
        old design has gui and logic mixed together
        The Model has DownloadItem as a base class and located at model.py module
        Model and controller has an observer system where model will notify controller when changed, in turn
        controller will update the current view
"""
import re
from datetime import datetime
import os, sys, time
from copy import copy
from threading import Thread
from queue import Queue
from datetime import date
from email.utils import parsedate_to_datetime

try:
    from ctypes import windll, wintypes, byref
except:
    pass

from . import update
from .utils import *
from . import setting
from . import config
from .config import Status, MediaType
from .brain import brain
from .model import ObservableDownloadItem, ObservableVideo


def set_option(**kwargs):
    """set global setting option(s) in config.py"""
    try:
        config.__dict__.update(kwargs)
        # log('Settings:', kwargs)
    except:
        pass


def get_option(key, default=None):
    """get global setting option(s) in config.py"""
    try:
        return config.__dict__.get(key, default)
    except:
        return None


def check_ffmpeg():
    return True


def write_timestamp(d):
    """write server timestamp to downloaded file

    try to figure out the timestamp of the remote file, and if available make
    the local file get that same timestamp.

    Args:
        d (ObservableDownloadItem): download item
    """

    try:

        if d.status == Status.completed:
            timestamp = ''

            try:
                # assume this is a video file, get upload date
                upload_date = d.vid_info.get('upload_date')  # YYYYMMDD e.g. 20201009
                timestamp = time.mktime(time.strptime(upload_date, '%Y%m%d'))
            except:
                pass

            if not timestamp:
                # get last modified timestamp from server,  eg.    'last-modified': 'Fri, 22 Feb 2019 09:30:09 GMT'
                headers = get_headers(d.eff_url, http_headers=d.http_headers)
                last_modified = headers.get('last-modified')

                if last_modified:
                    # parse timestamp
                    dt = parsedate_to_datetime(last_modified)
                    timestamp = dt.timestamp()  # will correct for local time
            if timestamp:
                log(f'writing timestamp "{timestamp}" to file: {d.name}', log_level=2)
                os.utime(d.target_file, (timestamp, timestamp))

                # modify creation time on windows,
                # credit: https://github.com/Delgan/win32-setctime/blob/master/win32_setctime.py
                if config.operating_system == 'Windows':
                    # Convert Unix timestamp to Windows FileTime using some magic numbers
                    timestamp = int((timestamp * 10000000) + 116444736000000000)
                    ctime = wintypes.FILETIME(timestamp & 0xFFFFFFFF, timestamp >> 32)

                    # Call Win32 API to modify the file creation date
                    handle = windll.kernel32.CreateFileW(d.target_file, 256, 0, None, 3, 128, None)
                    windll.kernel32.SetFileTime(handle, byref(ctime), None, None)
                    windll.kernel32.CloseHandle(handle)

    except Exception as e:
        log('controller.write_timestamp()> error:', e)
        if config.test_mode:
            raise e


def rename(d):
    """
    rename download item
    """
    forbidden_names = os.listdir(d.folder)  # + [d.name for d in self.d_map.values()]
    d.name = auto_rename(d.name, forbidden_names)
    d.calculate_uid()

    return d


def download_thumbnail(d):
    """download thumbnail

    Args:
        d (ObservableDownloadItem): download item
    """

    try:
        # download thumbnail
        if d.status == Status.completed and d.thumbnail_url:
            fp = os.path.splitext(d.target_file)[0] + '.png'
            download(d.thumbnail_url, fp=fp, decode=False)

    except Exception as e:
        log('controller._download_thumbnail()> error:', e)
        if config.test_mode:
            raise e


def log_runtime_info():
    """Print useful information about the system"""
    log('-' * 20, 'FireDM', '-' * 20)

    if config.isappimage:
        release_type = 'AppImage'
    elif config.FROZEN:
        release_type = 'Frozen'
    else:
        release_type = 'Non-Frozen'

    log('Starting FireDM version:', config.APP_VERSION, release_type)
    log('operating system:', config.operating_system_info)
    log('Python version:', sys.version)
    log('current working directory:', config.current_directory)
    log(f'FFMPEG: {config.ffmpeg_actual_path}, version: {config.ffmpeg_version}')


def create_video_playlist(*args, **kwargs):
    return []


def url_to_playlist(url, *args):
    d = ObservableDownloadItem()
    d.update(url)

    playlist = None

    if d.type:
        playlist = [d]

    return playlist


class Controller:
    """controller class
     communicate with (view / gui) and has the logic for downloading process

    it will update GUI thru an update_view method "refer to view.py" by sending data when model changes
    data will be passed in key, value kwargs and must contain "command" keyword

    example:
        {command='new', 'uid': 'uid_e3345de206f17842681153dba3d28ee4', 'active': True, 'name': 'hello.mp4', ...}

    command keyword could have the value of:
        'new':              gui should create new entry in its download list
        'update':           update current download list item
        'playlist_menu':    data contains a video playlist
        'stream_menu'       data contains stream menu
        'd_list'            an item in d_list, useful for loading d_list at startup

    uid keyword:
        this is a unique id for every download item which should be used in all lookup operations

    active keyword:
        to tell if data belongs to the current active download item

    """

    def __init__(self, view_class, custom_settings={}):
        self.observer_q = Queue()  # queue to collect references for updated download items

        # youtube-dl object
        self.ydl = None

        # d_map is a dictionary that map uid to download item object
        self.d_map = {}

        self.download_q = Queue()
        self.ignore_dlist = custom_settings.get('ignore_dlist', False)

        # load application settings
        self._load_settings()

        self.url = ''
        self.playlist = []
        self.last_active_playlist = None  # for playlist download
        self._playlist_menu = []
        self._stream_menu = []

        # create view
        self.view = view_class(controller=self)

        # observer thread, it will run in a different thread waiting on observer_q and call self._update_view
        Thread(target=self._observer, daemon=True).start()

        # handle download queue
        Thread(target=self.download_q_handler, daemon=True).start()

        # handle scheduled downloads
        Thread(target=self._scheduled_downloads_handler, daemon=True).start()

        # handle on completion actions
        Thread(target=self._on_completion_watchdog, daemon=True).start()

        # check for ffmpeg and update file path "config.ffmpeg_actual_path"
        check_ffmpeg()

    # region process url
    def auto_refresh_url(self, d):
        """refresh an expired url"""
        log('auto refresh url for:', d.name)
        url = d.url
        name = d.name
        folder = d.folder

        # refresh effective url for non video objects
        if d.type not in [MediaType.video, MediaType.audio]:
            # get headers
            headers = get_headers(url)

            eff_url = headers.get('eff_url')
            content_type = headers.get('content-type', '').split(';')[0]

            if content_type.lower() != 'text/html':
                d.eff_url = eff_url

        else:
            # process video
            playlist = create_video_playlist(url)
            if playlist:
                refreshed_d = playlist[0]

                # select video stream
                refreshed_d.select_stream(format_id=d.format_id, extension=d.extension, mediatype=d.type)
                log('selected stream:    ', d.selected_quality)
                log('New selected stream:', refreshed_d.selected_quality)

                # select audio stream
                if d.type == MediaType.video and 'dash' in d.subtype_list:
                    try:
                        match = [s for s in refreshed_d.audio_streams if s.name == d.audio_quality]
                        selected_audio_stream = match[0] if match else None
                        refreshed_d.select_audio(selected_audio_stream)
                        log('selected audio:    ', d.audio_quality)
                        log('New selected audio:', refreshed_d.audio_quality)
                    except:
                        pass

                # update old object
                d.__dict__.update(refreshed_d.__dict__)
                d.register_callback(self.observer)

        # restore original name and folder
        d.name = name
        d.folder = folder

        return d

    @threaded
    def process_url(self, url):
        """take url and return a a list of ObservableDownloadItem objects

        when a "view" call this method it should expect a playlist menu (list of names) to be passed to its update
        method,

        Examples:
            playlist_menu=['1- Nasa mission to Mars', '2- how to train your dragon', ...]
            or
            playlist_menu=[] if no video playlist

        """
        if not url:
            return

        self.reset()
        self.url = url

        playlist = []

        d = ObservableDownloadItem()
        d.update(url)

        if d.type:
            playlist = [d]

        if not playlist and d.type:
            playlist = [d]

        if url == self.url:
            self.playlist = playlist
            self._update_playlist_menu([])

            if self.playlist:
                d = playlist[0]
                self.report_d(d, active=True)

        return playlist

    # endregion

    # region update view
    def observer(self, **kwargs):
        """This is an observer method which get notified when change/update properties in ObservableDownloadItem
        it should be as light as possible otherwise it will impact the whole app
        it will be registered by ObservableDownloadItem while creation"""

        self.observer_q.put(kwargs)

    def _observer(self):
        """run in a thread and update views once there is a change in any download item
        it will update gui/view only on specific time intervals to prevent flooding view with data

        example of an  item in self.observer_q: {'uid': 'fdsfsafsddsfdsfds', 'name': 'some_video.mp4', ...}
        every item must have "uid" key
        """

        buffer = {}  # key = uid, value = kwargs
        report_interval = 0.5  # sec

        while True:
            for i in range(self.observer_q.qsize()):
                item = self.observer_q.get()
                uid = item.get('uid')
                if uid:
                    buffer.setdefault(uid, item).update(**item)

            for v in buffer.values():
                self._update_view(**v)

            buffer.clear()

            time.sleep(report_interval)

    def _update_view(self, **kwargs):
        """update "view" by calling its update method"""
        # print('controller._update_view:', kwargs)
        try:
            # set default command value
            kwargs.setdefault('command', 'update')

            uid = kwargs.get('uid')
            d = self.d_map.get(uid, None)

            if d is not None:
                # readonly properties will not be reported by ObservableDownloadItem
                downloaded = kwargs.get('downloaded', None)
                if downloaded:
                    extra = {k: getattr(d, k, None) for k in ['progress', 'speed', 'eta']}
                    # print('extra:', extra)

                    kwargs.update(**extra)

            self.view.update_view(**kwargs)
            # print('controller._update_view:', kwargs)
        except Exception as e:
            log('controller._update_view()> error, ', e)
            if config.test_mode:
                raise e

    @threaded
    def report_d(self, d=None, uid=None, video_idx=None, **kwargs):
        """notify view of all properties of a download item

        Args:
            d (ObservableDownloadItem or ObservableVideo): download item
            kwargs: key, values to be included
        """

        d = d or self.get_d(uid, video_idx)
        if not d:
            return

        properties = d.watch_list

        info = {k: getattr(d, k, None) for k in properties}

        if d in self.playlist:
            info.update(video_idx=self.playlist.index(d))

        info.update(**kwargs)

        self._update_view(**info)

    # endregion

    # region settings
    def _load_settings(self, **kwargs):
        if not self.ignore_dlist:
            # load stored setting from disk
            # setting.load_setting()

            # load d_map
            self.d_map = setting.load_d_map()

            # register observer
            for d in self.d_map.values():
                d.register_callback(self.observer)

        # # update config module with custom settings
        # config.__dict__.update(**kwargs)

    def save_d_map(self):
        if not self.ignore_dlist:
            setting.save_d_map(self.d_map)

    # endregion

    # region video

    def _update_playlist_menu(self, pl_menu):
        pass

    @threaded
    def get_stream_menu(self, d=None, uid=None, video_idx=None):
        pass

    def select_stream(self, stream_idx, uid=None, video_idx=None, d=None, report=True, active=True):
        pass

    def select_audio(self, audio_idx, uid=None, video_idx=None, active=True):
        pass

    def set_video_backend(self, extractor):
        pass

    # endregion

    # region video playlist
    def get_playlist_titles(self):
        return None

    def prepare_playlist(self):
        pass

    @threaded
    def download_playlist(self, download_info, **kwargs):
        pass

    # endregion

    # region download
    def download_q_handler(self):
        """handle downloads, should run in a dedicated thread"""

        while True:
            active_downloads = len([d for d in self.d_map.values() if d.status in Status.active_states])
            if active_downloads < config.max_concurrent_downloads:
                d = self.download_q.get()
                if d.status == Status.pending:
                    self._download(d)

            time.sleep(1)

    def _scheduled_downloads_handler(self):
        """handle scheduled downloads, should run in a dedicated thread"""

        while True:
            sched_downloads = [d for d in self.d_map.values() if d.status == Status.scheduled]
            if sched_downloads:
                current_datetime = datetime.now()
                for d in sched_downloads:
                    if d.sched and datetime.fromisoformat(d.sched) <= current_datetime:
                        self.download(d, silent=True)

            time.sleep(60)

    def _pre_download_checks(self, d, silent=False, force_rename=False):
        """do all checks required for this download

        Args:
        d: ObservableDownloadItem object
        silent: if True, hide all a warning dialogues and select default

        Returns:
            (bool): True on success, False on failure
        """

        showpopup = not silent

        if not (d or d.url):
            log('Nothing to download', start='', showpopup=showpopup)
            return False
        elif not d.type or d.type == 'text/html':
            if not silent:
                response = self.get_user_response(popup_id=1)
                if response == 'Ok':
                    d.accept_html = True
            else:
                return False

        if d.status in Status.active_states:
            log('download is already in progress for this item')
            return False

        # check unsupported protocols
        unsupported = ['f4m', 'ism']
        match = [item for item in unsupported if item in d.subtype_list]
        if match:
            log(f'unsupported protocol: \n"{match[0]}" stream type is not supported yet', start='', showpopup=showpopup)
            return False

        # check for ffmpeg availability
        if d.type in (MediaType.video, MediaType.audio, MediaType.key):
            if not check_ffmpeg():

                if not silent and config.operating_system == 'Windows':
                    res = self.get_user_response(popup_id=2)
                    if res == 'Download':
                        # download ffmpeg from github
                        self._download_ffmpeg()
                else:
                    log('FFMPEG is missing', start='', showpopup=showpopup)

                return False

        # in case of missing download folder value will fallback to current download folder
        folder = d.folder or config.download_folder

        # validate destination folder for existence and permissions
        try:
            # write test file to download folder
            test_file_path = os.path.join(folder, 'test_file_.firedm')
            # skip test in case test_file already created by another thread
            if not os.path.isfile(test_file_path):
                with open(test_file_path, 'w') as f:
                    f.write('0')
                delete_file(test_file_path)

            # update download item
            d.folder = folder
        except FileNotFoundError:
            log(f'destination folder {folder} does not exist', start='', showpopup=showpopup)
            if config.test_mode:
                raise
            return False
        except (PermissionError, OSError):
            log(f"you don't have enough permission for destination folder {folder}", start='', showpopup=showpopup)
            if config.test_mode:
                raise
            return False
        except Exception as e:
            log(f'problem in destination folder {repr(e)}', start='', showpopup=showpopup)
            if config.test_mode:
                raise e
            return False

        # validate file name
        if not d.name:
            log("File name can't be empty!!", start='', showpopup=showpopup)
            return False

        # check if file with the same name exist in destination --------------------------------------------------------
        if os.path.isfile(d.target_file):

            # auto rename option
            if config.auto_rename or silent:
                action = 'Rename'
            else:
                #  show dialogue
                action = self.get_user_response(popup_id=4)

                if action not in ('Overwrite', 'Rename'):
                    log('Download cancelled by user')
                    return False

            if action == 'Rename':
                rename(d)
                log('File with the same name exist in download folder, generate new name:', d.name)
                return self._pre_download_checks(d, silent=silent)
            elif action == 'Overwrite':
                delete_file(d.target_file)

        # search current list for previous item with same name, folder ---------------------------
        if d.uid in self.d_map:
            # log('download item', d.uid, 'already in list, check resume availability')

            # get download item from the list
            d_from_list = self.d_map[d.uid]

            if force_rename:
                forbidden_names = os.listdir(d.folder) + [d.name for d in self.d_map.values()]
                d.name = auto_rename(d.name, forbidden_names)
                d.calculate_uid()

            # if match ---> resume, else rename
            elif d.total_size == d_from_list.total_size:
                # don't resume active items'
                if d_from_list.status in Status.active_states:
                    log('download is already in progress for this item')
                    return False

                log('resume is possible')
                d.downloaded = d_from_list.downloaded
            else:
                log('Rename File')
                rename(d)
                return self._pre_download_checks(d, silent=silent)

        # ------------------------------------------------------------------

        # warning message for non-resumable downloads
        if not d.resumable and not silent:
            res = self.get_user_response(popup_id=5)
            if res != 'Yes':
                return False

        # if above checks passed will return True
        return True

    def download(self, d=None, uid=None, video_idx=None, silent=False, download_later=False, **kwargs):
        showpopup = not silent

        d = d or self.get_d(uid, video_idx)
        if not d:
            log('Nothing to download', showpopup=showpopup)
            return False
        status = d.status
        if status == Status.pending:
            log('item already pending ...')
            return False

        # make a copy of d to prevent changes in self.playlist items
        d = copy(d)
        d.status = status

        update_object(d, kwargs)

        pre_checks = self._pre_download_checks(d, silent=silent, force_rename=kwargs.get('force_rename', False))
        # print('precheck:', pre_checks)

        if pre_checks:
            # update view
            self.report_d(d, command='new')

            # register observer
            d.register_callback(self.observer)

            # add to download map
            self.d_map[d.uid] = d

            # save on disk
            self.save_d_map()

            if not download_later:
                d.status = Status.pending
                self.download_q.put(d)

            return True
        else:
            return False

    @threaded
    def _download(self, d, **kwargs):

        # retry multiple times to download and auto refresh expired url
        for n in range(config.refresh_url_retries + 1):
            # start brain in a separate thread
            t = Thread(target=brain, daemon=False, args=(d,))
            t.start()

            # wait thread to end
            t.join()

            if d.status != Status.error:
                break

            elif n >= config.refresh_url_retries:
                log('controller: too many connection errors', 'maybe network problem or expired link')
            else:  # try auto refreshing url
                # reset errors and change status
                d.status = Status.refreshing_url
                d.errors = 0

                # update view
                self.report_d(d)

                # refresh url
                self.auto_refresh_url(d)

        # update view
        self.report_d(d)

        # actions to be done after completing download
        self._post_download(d)

        # report completion
        if d.status == Status.completed:
            log(f"File: {d.name}, saved at: {d.folder}")

    def stop_download(self, uid):
        """stop downloading
        Args:
            uid (str): unique identifier property for a download item in self.d_map
        """

        d = self.d_map.get(uid)

        if d and d.status in (*Status.active_states, Status.pending):
            d.status = Status.cancelled

    def _post_download(self, d):
        """actions required after done downloading

        Args:
            d (ObservableDownloadItem): download item
        """

        # on completion actions
        if d.status == Status.completed:
            if config.download_thumbnail:
                download_thumbnail(d)

            if config.checksum:
                log()
                log(f'Calculating MD5 and SHA256 for {d.target_file} .....')
                md5, sha256 = calc_md5_sha256(fp=d.target_file)
                log(f'MD5: {md5} - for {d.name}')
                log(f'SHA256: {sha256} - for {d.name}')

            if config.use_server_timestamp:
                write_timestamp(d)

            if d.on_completion_command:
                err, output = run_command(d.on_completion_command)
                if err:
                    log(f'error executing command: {d.on_completion_command} \n{output}')

            if d.shutdown_pc:
                d.shutdown_pc = False
                self.shutdown_pc()

    def _download_ffmpeg(self, destination=config.sett_folder):
        """download ffmpeg.exe for windows os

        Args:
            destination (str): download folder

        """

        # set download folder
        config.ffmpeg_download_folder = destination

        # first check windows 32 or 64
        import platform
        # ends with 86 for 32 bit and 64 for 64 bit i.e. Win7-64: AMD64 and Vista-32: x86
        if platform.machine().endswith('64'):
            # 64 bit link
            url = 'https://github.com/firedm/FireDM/releases/download/extra/ffmpeg_64bit.exe'
        else:
            # 32 bit link
            url = 'https://github.com/firedm/FireDM/releases/download/extra/ffmpeg_32bit.exe'

        log('downloading: ', url)

        # create a download object, will save ffmpeg in setting folder
        d = ObservableDownloadItem(url=url, folder=config.ffmpeg_download_folder)
        d.update(url)
        d.name = 'ffmpeg.exe'

        self.download(d, silent=True)

    def autodownload(self, url, **kwargs):
        """download file automatically without user intervention
        for video files it should download best quality, for video playlist, it will download first video
        """

        stream_options = kwargs.setdefault('stream_options', {})
        download_options = kwargs.setdefault('download_options', {})
        subtitles = kwargs.get('subtitles', {})

        playlist = url_to_playlist(url)
        d = playlist[0]
        update_object(d, kwargs)

        # update download folder
        folder = download_options.get('folder', None)
        if folder:
            d.folder = folder

        # download item
        self.download(d, silent=True, **download_options, **kwargs)

        if subtitles:
            self.download_subtitles(subtitles, d=d)

    @threaded
    def batch_download(self, urls, **kwargs):
        urls_ = "\n".join(urls)
        log(f'Downloading the following url(s):\n{urls_}')
        # print('Batch download options:', kwargs)

        for url in urls:
            if config.shutdown:
                print('batch_download()> config.shutdown is true, terminating')
                break
            kwargs['force_rename'] = True
            self.autodownload(url, **kwargs)
            time.sleep(0.5)

    # endregion

    # region Application update
    @threaded
    def check_for_update(self, signal_id=None, wait=False, timeout=30, **kwargs):
        """check for newer version of FireDM, youtube-dl, and yt_dlp
        Args:
            signal_id(any): signal a view when this function done
            wait(bool): wait for youtube-dl and ytdlp to load
            timeout(int): timeout for above wait in seconds
        """

        if wait:
            c = 1
            while config.youtube_dl_version is None or config.yt_dlp_version is None:
                log('\ryoutube-dl and ytdlp still loading, please wait', '.' * c, end='')
                c += 1
                if c > timeout:
                    break
                time.sleep(1)
            log()

        info = {'firedm': {'current_version': config.APP_VERSION, 'latest_version': None},
                'awesometkinter': {'current_version': config.atk_version, 'latest_version': None},
                }

        def fetch_pypi(pkg):
            pkg_info = info[pkg]
            pkg_info['latest_version'], pkg_info['url'] = update.get_pkg_latest_version(pkg, fetch_url=True)
            log('done checking:', pkg, 'current:', pkg_info['current_version'], 'latest:', pkg_info['latest_version'])

        threads = []
        pkgs = info.keys()
        for pkg in pkgs:
            if not info[pkg]['current_version']:
                log(f'{pkg} still loading, try again')
                continue
            t = Thread(target=fetch_pypi, args=(pkg,))
            threads.append(t)
            t.start()
            time.sleep(0.1)

        for t in threads:
            t.join()

        # update
        msg = 'Check for update Status:\n\n'
        new_pkgs = []
        for pkg in pkgs:
            pkg_info = info[pkg]
            current_version = pkg_info['current_version']
            latest_version = pkg_info['latest_version']

            if current_version is None:
                msg += f'    {pkg}: still loading, try again!\n\n'
            elif latest_version is None:
                msg += f'    {pkg}: check for update .... Failed!\n\n'
            elif update.parse_version(latest_version) > update.parse_version(current_version):
                msg += f'    {pkg}: New version "{latest_version}" Found!\n\n'
                new_pkgs.append(pkg)
            else:
                msg += f'    {pkg}: up to date!\n\n'

        if new_pkgs:
            msg += 'Do you want to update now? \n'
            options = ['Update', 'Cancel']

            # show update notes for firedm
            if 'firedm' in new_pkgs:
                log('getting FireDM changelog ....')

                # download change log file
                url = 'https://github.com/firedm/FireDM/raw/master/ChangeLog.txt'
                changelog = download(url, verbose=False)

                # verify server didn't send html page
                if changelog and '<!DOCTYPE html>' not in changelog:
                    msg += '\n\n\n'
                    msg += 'FireDM Change Log:\n'
                    msg += changelog

            res = self.get_user_response(msg, options)
            if res == options[0]:

                # check write permission
                tf = update.get_target_folder('firedm')
                if tf and not check_write_permission(tf):
                    log('Permission error:',
                        'Run FireDM as admin to install updates', showpopup=True)
                    return

                # start updating modules
                done_pkgs = {}
                for pkg in new_pkgs:
                    pkg_info = info[pkg]
                    latest_version, url = pkg_info['latest_version'], pkg_info['url']

                    log('Installing', pkg, latest_version)
                    try:
                        success = update.update_pkg(pkg, url)
                        done_pkgs[pkg] = success

                    except Exception as e:
                        log(f'failed to update {pkg}:', e)

                msg = 'Update results:\n\n'
                for pkg, success in done_pkgs.items():
                    msg += f'{pkg} - {"Updated Successfully!" if success else "Update Failed!"}\n\n'

                if any(done_pkgs.values()):
                    msg += 'Please Restart application for update to take effect!'
                else:
                    msg += 'Update failed!!!! ... try again'

                log(msg, showpopup=True)

        else:
            log(msg, showpopup=True)

        # tell view we are done
        if signal_id is not None:
            self._update_view(command='signal', signal_id=signal_id)

        today = date.today()
        config.last_update_check = (today.year, today.month, today.day)

    @threaded
    def auto_check_for_update(self):
        """auto check for firedm update"""
        if config.check_for_update and not config.disable_update_feature:
            today = date.today()

            if update.parse_version(config.APP_VERSION) > update.parse_version(config.updater_version):
                config.last_update_check = (today.year, today.month, today.day)
                config.updater_version = config.APP_VERSION
                # log('Running newer FireDM version, reset last_update_check')

            else:
                try:
                    last_check = date(*config.last_update_check)
                except:
                    last_check = today
                    config.last_update_check = (today.year, today.month, today.day)

                delta = today - last_check
                if delta.days >= config.update_frequency:
                    res = self.get_user_response(f'Check for FireDM update?\nLast check was {delta.days} days ago',
                                                 options=['Ok', 'Cancel'])
                    if res == 'Ok':
                        self.check_for_update()

    # endregion

    # region subtitles

    def download_subtitles(self, subs, uid=None, video_idx=None, d=None):
        pass

    # endregion

    # region file/folder operations
    def play_file(self, uid=None, video_idx=None):
        """open download item target file or temp file"""
        # get download item
        d = self.get_d(uid, video_idx)

        if not d:
            return

        fp = d.target_file if os.path.isfile(d.target_file) else d.temp_file

        open_file(fp, silent=True)

    def open_file(self, uid=None, video_idx=None):
        # get download item
        d = self.get_d(uid, video_idx)

        if not d:
            return

        open_file(d.target_file)

    def open_temp_file(self, uid=None, video_idx=None):
        # get download item
        d = self.get_d(uid, video_idx)

        if not d:
            return

        open_file(d.temp_file)

    def open_folder(self, uid=None, video_idx=None):
        # get download item
        d = self.get_d(uid, video_idx)

        if not d:
            return

        open_folder(d.folder)

    @threaded
    def delete(self, uid, deltarget=False):
        """delete download item from the list
        Args:
            uid (str): unique identifier property for a download item in self.d_map
            deltarget(bool): if True it will delete target file on disk
        """

        d = self.d_map.pop(uid)

        d.status = Status.cancelled

        # delete files
        d.delete_tempfiles()

        # delete target file
        if deltarget:
            delete_file(d.target_file)

    # endregion

    # region get info
    def get_property(self, property_name, uid=None, video_idx=None):
        d = self.get_d(uid, video_idx)

        if not d:
            return

        return getattr(d, property_name, None)

    @threaded
    def get_d_list(self):
        """update previous download list in view"""
        log('controller.get_d_list()> sending d_list')

        buff = {'command': 'd_list', 'd_list': []}
        for d in self.d_map.values():
            properties = d.watch_list
            info = {k: getattr(d, k, None) for k in properties}
            buff['d_list'].append(info)
        self.view.update_view(**buff)

    def get_segments_progress(self, uid=None, video_idx=None):
        # get download item
        d = self.get_d(uid, video_idx)

        if not d:
            return None

        return d.update_segments_progress(activeonly=False)

    def get_properties(self, uid=None, video_idx=None):
        # get download item
        d = self.get_d(uid, video_idx)

        if not d:
            return 'No properties available!'

        # General properties
        text = f'UID: {d.uid} \n' \
               f'Name: {d.name} \n' \
               f'Folder: {d.folder} \n' \
               f'Progress: {d.progress}% \n' \
               f'Downloaded: {format_bytes(d.downloaded)} of {format_bytes(d.total_size)} \n' \
               f'Status: {d.status} \n' \
               f'Resumable: {d.resumable} \n' \
               f'Type: {d.type}, {", ".join(d.subtype_list)}\n' \
               f'Remaining segments: {d.remaining_parts} of {d.total_parts}\n'

        if d.type == 'video':
            text += f'Protocol: {d.protocol} \n' \
                    f'Video stream: {d.selected_quality}\n'

            if 'dash' in d.subtype_list:
                text += f'Audio stream: {d.audio_quality}\n'

        if d.status == Status.scheduled:
            text += f'Scheduled: {d.sched}'

        return text

    def get_d(self, uid=None, video_idx=None):
        """get download item reference

        Args:
            uid (str): unique id for a download item
            video_idx (int): index of a video download item in self.playlist

        Returns:
            (DownloadItem): if uid and video_idx omitted it will return the first object in self.playlist
        """

        try:
            if uid:
                d = self.d_map.get(uid)
            elif video_idx:
                d = self.playlist[video_idx]
            else:
                d = self.playlist[0]
        except:
            d = None

        return d

    # endregion

    # region schedul
    def schedule_start(self, uid=None, video_idx=None, target_date=None):
        """Schedule a download item
        Args:
            target_date (datetime.datetime object): target date and time to start download
        """
        # get download item
        d = self.get_d(uid, video_idx)

        if not d or not isinstance(target_date, datetime):
            return

        # validate target date should be greater than current date
        if target_date < datetime.now():
            log('Can not Schedule something in the past', 'Please select a Schedule time greater than current time',
                showpopup=True)
            return

        log(f'Schedule {d.name} at: {target_date}')
        d.sched = target_date.isoformat(sep=' ')
        d.status = Status.scheduled

    def schedule_cancel(self, uid=None, video_idx=None):
        # get download item
        d = self.get_d(uid, video_idx)

        if not d or d.status != Status.scheduled:
            return

        log(f'Schedule for: {d.name} has been cancelled')
        d.status = Status.cancelled
        d.sched = None

    # endregion

    # region on completion command / shutdown
    def _on_completion_watchdog(self):
        """a separate thread to watch when "ALL" download items are completed and execute on completion action if
        configured"""

        # make sure user started any item downloading, after setting "on-completion actions"
        trigger = False

        while True:
            if config.shutdown:
                break

            # check for "on-completion actions"
            if config.on_completion_command or config.shutdown_pc or config.on_completion_exit:
                # check for any active download, then set the trigger
                if [d for d in self.d_map.values() if d.status in Status.active_states]:
                    trigger = True

                elif trigger:
                    # check if items no longer active or pending
                    if not [d for d in self.d_map.values() if d.status in Status.active_states or d.status == Status.pending]:
                        # reset the trigger
                        trigger = False

                        # execute command
                        if config.on_completion_command:
                            run_command(config.on_completion_command)

                        # shutdown
                        if config.shutdown_pc:
                            self.shutdown_pc()

                        # exit application
                        if config.on_completion_exit:
                            self.quit()
            else:
                trigger = False

            time.sleep(5)

    def scedule_shutdown(self, uid):
        """schedule shutdown after an item completed downloading"""
        d = self.get_d(uid=uid)
        if d.status == Status.completed:
            return

        d.shutdown_pc = True

    def cancel_shutdown(self, uid):
        """cancel pc shutdown scedule for an item"""
        d = self.get_d(uid=uid)
        if d.shutdown_pc:
            d.shutdown_pc = False
            log('shutdown schedule cancelled for:', d.name)

    def toggle_shutdown(self, uid):
        """set shutdown flag on/off"""
        d = self.get_d(uid=uid)
        if d.status == Status.completed:
            return
        d.shutdown_pc = not d.shutdown_pc

    def shutdown_pc(self):
        """shut down computer"""
        if config.operating_system == 'Windows':
            cmd = 'shutdown -s -t 120'
            abort_cmd = 'shutdown -a'
        else:
            # tested on pop os, but it might needs root privillage on other distros.
            cmd = 'shutdown --poweroff +2'
            abort_cmd = 'shutdown -c'

        # save settings
        self.save_d_map()

        err, output = run_command(cmd)
        if err:
            log('error:', output, showpopup=True)
            return

        res = self.get_user_response('your device will shutdown after 2 minutes \n'
                                     f'{output} \n'
                                     'press "ABORT!" to cancel', options=['ABORT!'])
        if res == 'ABORT!':
            run_command(abort_cmd)
        else:
            self.view.hide()
            self.view.quit()

    def set_on_completion_command(self, uid, command):
        d = self.get_d(uid=uid)
        if d.status == Status.completed:
            return
        d.on_completion_command = command

    def get_on_completion_command(self, uid):
        d = self.get_d(uid=uid)
        return d.on_completion_command

    # endregion

    # region general
    def get_user_response(self, msg='', options=[], popup_id=None):
        """get user response from current view

        Args:
            msg(str): a message to show
            options (list): a list of options, example: ['yes', 'no', 'cancel']
            popup_id(int): popup id number in config.py

        Returns:
            (str): response from user as a selected item from "options"
        """

        if popup_id:
            popup = config.get_popup(popup_id)
            msg = popup['body']
            options = popup['options']
            if not popup['show']:
                return popup['default']

        res = self.view.get_user_response(msg, options, popup_id=popup_id)

        return res

    def run(self):
        """run current "view" main loop"""
        self.view.run()

    def quit(self):
        config.shutdown = True  # set global shutdown flag
        config.ytdl_abort = True

        # cancel all current downloads
        for d in self.d_map.values():
            self.stop_download(d.uid)

        self.save_d_map()
        self.view.quit()

    def reset(self):
        """reset controller and cancel ongoing operation"""
        # stop youyube-dl
        self.url = ''
        config.ytdl_abort = True
        self.playlist = []

    # endregion

    # region cmdline
    def cmdline_download(self, urls, **kwargs):
        """handle command line downloads"""
        for url in urls:
            playlist = url_to_playlist(url)
            d = playlist[0]

            update_object(d, kwargs)

            # precheck
            if os.path.isfile(d.target_file) and config.auto_rename:
                d.name = auto_rename(d.name, forbidden_names=os.listdir(d.folder))
                log('file already exist, auto-rename to:', d.name)

            # update view
            self.report_d(d, command='new', threaded=False)

            # register observer
            d.register_callback(self.observer)

            # add to download map
            self.d_map[d.uid] = d

            self._download(d, **kwargs, threaded=False)

            # update view
            self.report_d(d, threaded=False)

    def interactive_download(self, url, **kwargs):
        pass

