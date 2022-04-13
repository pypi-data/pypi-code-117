import logging
import requests
import json
import numpy as np
import PIL
import io

class connector():
    def __init__(self, key, url="https://project-kiwi.org/api/"):
        """constructor

        Args:
            key (str): API key.
            url (str, optional): url for api, in case of multiple instances. Defaults to "https://project-kiwi.org/api/".

        Raises:
            ValueError: API key must be supplied.
        """        
        if key is None:
            raise ValueError("API key missing")

        self.key = key
        self.url = url


    def getImagery(self, project=None):
        """Get a list of imagery

        Args:
            project (str, optional): ID of the project to get all the imagery for, by default, all projects associated with user.

        Returns:
            json: list of imagery
        """        
        route = "get_imagery"
        params = {'key': self.key}
        if not project is None:
            params['project'] = project
        r = requests.get(self.url + route, params=params)
        r.raise_for_status()
        jsonResponse = r.json()
        return jsonResponse


    def getTiles(self, imageryId: str):
        """Get a list of tiles for a given imagery id

        Args:
            imageryId (str): ID of the imagery to retrieve a list of tiles for

        Returns:
            list: list of tile urls
        """        
        route = "get_tile_list"
        params = {'key': self.key, 'imagery_id': imageryId}

        r = requests.get(self.url + route, params=params)
        r.raise_for_status()
        jsonResponse = r.json()
        return jsonResponse

    def getTile(self, url):
        """Get a tile in numpy array form

        Args:
            url (str): url of the tile

        Returns:
            np.array: numpy array containing the tile
        """
        r = requests.get(url)
        r.raise_for_status()
        tileContent = r.content
        return np.array(PIL.Image.open(io.BytesIO(tileContent)))


    def getTileDict(self, imageryId: str):
        """Get a dictionary of tiles for a given imagery id

        Args:
            imageryId (str): ID of the imagery to retrieve a list of tiles for

        Returns:
            dict: a dictionary of tiles with zxy keys
        """        
        route = "get_tile_list"
        params = {'key': self.key, 'imagery_id': imageryId}

        r = requests.get(self.url + route, params=params)
        r.raise_for_status()
        jsonResponse = r.json()
        dict = {}
        for tile in jsonResponse:
            dict[tile['zxy']] = tile['url']
        return dict



    def getImageryStatus(self, imageryId: str):
        """ Get the status of imagery

        Args:
            imageryId (str): Imagery id

        Returns:
            str: status
        """        
        route = "get_imagery_status"
        params = {'key': self.key, 'imagery_id': imageryId}

        r = requests.get(self.url + route, params=params)
        r.raise_for_status()
        return r.json()['status']


    def setImageryStatus(self, imageryId: str, status: str):
        """Set the status for imagery e.g. when the upload is complete

        Args:
            imageryId (str): Imagery id
            status (str): status e.g. "awaiting processing"
        """
        route = "set_imagery_status" 
        params = {'key': self.key, 'imagery_id': imageryId, 'status': status}

        r = requests.get(self.url + route, params=params)
        r.raise_for_status()



    def addImagery(self, filename: str, name: str):
        """ Add imagery to project-kiwi.org

        Args:
            filename (str): Path to the file to be uploaded
            name (str): Name for the imagery

        Returns:
            int: imagery id
        """       
        
        # get presigned upload url
        route = "get_imagery_upload_url"
        params = {'key': self.key, 'filename': filename, 'name': name}
        r = requests.get(self.url + route, params=params)
        r.raise_for_status()
        jsonResponse = r.json()
        url = jsonResponse['url']
        
        # upload
        r = requests.put(url, data=open(filename, 'rb'), headers={'Content-type': ''})
        r.raise_for_status()

        # set the status - triggers processing
        self.setImageryStatus(jsonResponse['imagery_id'], "awaiting processing")
        return jsonResponse['imagery_id']
        
        



