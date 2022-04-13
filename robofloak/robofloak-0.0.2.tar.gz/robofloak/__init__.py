from robofloak.pipe import DepthAIPipeline, list_devices
from robofloak.api import download_blob
import os
import json
import threading
from pip._internal.utils.appdirs import user_cache_dir
import shutil

cache_dir = user_cache_dir('pip') + "/roboflow"

class OAK:
    def __init__(self, project, version, api_key, rgb=False, depth=False, device=None, blocking=True, legacy=False):
        self.project = project
        self.version = version
        self.api_key = api_key
        self.blocking = blocking

        self.dev = device

        if self.dev is None:
            available_devices = list_devices()
            if len(available_devices) == 0:
                raise Exception("No available OAK devices detected.")
                default_device = None
            else:
                self.dev = available_devices[0]

        self.cache_path = self.find_weights()
        with open(os.path.join(self.cache_path, 'config.txt'), 'r') as f:
            self.model_objects = json.loads(f.read())
            self.size = (int(self.model_objects["environment"]["RESOLUTION"]), int(self.model_objects["environment"]["RESOLUTION"]))
            self.resolution = self.size
            self.class_names = self.model_objects["class_names"]
            self.colors = self.model_objects["colors"]
        try:
            self.dai_pipe = DepthAIPipeline(self.cache_path+"/roboflow.blob", self.size, self.resolution, self.class_names, rgb, self.colors, False, depth, device, legacy)
        except:
            try:
                shutil.rmtree(cache_dir)
                self.cache_path = self.find_weights()
                with open(os.path.join(self.cache_path, 'config.txt'), 'r') as f:
                    self.model_objects = json.loads(f.read())
                    self.size = (int(self.model_objects["environment"]["RESOLUTION"]), int(self.model_objects["environment"]["RESOLUTION"]))
                    self.resolution = self.size
                    self.class_names = self.model_objects["class_names"]
                    self.colors = self.model_objects["colors"]
                self.dai_pipe = DepthAIPipeline(self.cache_path+"/roboflow.blob", self.size, self.resolution, self.class_names, rgb, self.colors, False, depth, device, legacy)
            except:
                raise Exception("Failure while retrying load weights - does this model, version, api key exist? can you curl api.roboflow.com, and can your device download files from google cloud storage? have you hit your device limit?")

    def find_weights(self):
        if os.path.exists(os.path.join(cache_dir, self.project, self.version, "roboflow.blob")) and os.path.exists(
                        os.path.join(cache_dir, self.project, self.version, "config.txt")):
            return os.path.join(cache_dir, self.project, self.version)

        return download_blob(self.project, self.version, self.api_key, self.dev)

    def detections(self):
        if self.blocking:
            return self.dai_pipe.get()
        return self.dai_pipe.try_get()

class OAKThread(threading.Thread, OAK):
    def __init__(self, threadID, name, counter, onDetect, project, version, api_key, rgb=True, depth=False, device=None, blocking=True, legacy=False):
        OAK.__init__(self, project, version, api_key, rgb, depth, device, blocking, legacy)
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.onDetect = onDetect

    def run(self):
        while True:
            detections, frame, raw_frame, depth = self.detections()
            self.onDetect(self.threadID, detections, frame, raw_frame, depth)



def devices():
    return list_devices()



