import requests
import urllib.request
from CONSTANTS import CONST
import mp3play
class DownloadHolo:
    def Download():
        req_download = CONST.download_holoearth_str
        urllib.request.urlretrieve(req_download, "Holoearth.zip")