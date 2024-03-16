import dearpygui.dearpygui as dpg
import ctypes
import download_holoearth
import os
import tkinter.messagebox as mbox
import time
import Unzipper
def DownloadFile():
    download_holoearth.DownloadHolo.Download()
    while os.path.isdir("E:\\Program Files\\MadeByRiritoNinigaya\\HoloEarthLauncher"):
        time.sleep(5)
        if os.path.isfile("E:\\Program Files\\MadeByRiritoNinigaya\\HoloEarthLauncher\\Holoearth.zip"):
            if mbox.askyesno(title="Holoearth Launcher", message="Download Is Completed... Do you want to unzip?!") == mbox.YES:
                Unzipper.Unzip_File.Unzip("Holoearth.zip", dpg.get_value("tag_pathval"))
            else:
                mbox.showinfo(title="Holoearth Launcher", message="Okay... You can Manually Unzip into You're Created Folder or something else")
                exit(3102)
def UI_Main():
    width, height, channels, data = dpg.load_image("{}".format(os.getcwd() + "\\Assets\\HoloearthDPG.bmp"))
    dpg.create_context()
    dpg.create_viewport(title="HoloearthLauncher by RiritoNinigaya", width=955, height=1200)
    with dpg.font_registry():
        finserif = dpg.add_font("{}".format(os.getcwd() + "\\Assets\\FinSerifDisp.otf"), size=15)
    with dpg.texture_registry():
        holoearth_image = dpg.add_static_texture(width, height, data)
    with dpg.window(label="Holoearth Launcher", tag='hololive_launcher'):
        with dpg.tab_bar():
            with dpg.tab(label="Downloader"):
                dpg.add_image(holoearth_image)
                dpg.add_input_text(label="Path To Download File", tag="tag_pathval")
                dpg.add_button(label="Download Holoearth Game", callback=DownloadFile)
        dpg.bind_font(finserif)
    dpg.create_viewport(title='HoloearthLauncher by RiritoNinigaya', width=920, height=1200)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("hololive_launcher", True)
    dpg.start_dearpygui()
    dpg.destroy_context()
