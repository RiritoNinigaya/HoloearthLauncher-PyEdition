import requests
import urllib.request
from CONSTANTS import CONST
import mp3play
import os
class DownloadHolo:
    def Download():
        req_download = str(CONST.download_holoearth_str)
        urllib.request.urlretrieve(req_download, "{}".format(os.getcwd() + "\\Holoearth.zip"))
