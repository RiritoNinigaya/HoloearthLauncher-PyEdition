import zipfile

class Unzip_File:
    def Unzip(file_name : str, dest : str):
        with zipfile.ZipFile(file_name,"r") as zip_ref:
            zip_ref.extractall(dest)