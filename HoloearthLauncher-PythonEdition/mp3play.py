import ctypes
import os
def PlayMP3():
    return ctypes.cdll.LoadLibrary("Winmm.dll").mciSendStringW("play music.mp3 repeat", 0, 0 , 0)