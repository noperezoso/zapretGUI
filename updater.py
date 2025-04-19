import requests
import os
from shutil import rmtree
from zipfile import ZipFile


class Updater:
    def __init__(self, name=None, try_mirror=False):
        default_url = 'https://github.com/bol-van/zapret-win-bundle/archive/refs/heads/master.zip'
        self.name = 'zapret-win-bundle-master' if not name else name
        if requests.head(default_url).status_code < 400:
            self.url = default_url
        else:
            self.url = None


    def get_zapret(self, url, name, force=False):
        '''Download and unpack zapret software.'''
        name = 'zapret-win-bundle-master'
        def download():
            request = requests.get(url)
            with open(f'{name}.zip', 'wb') as archive:
                archive.write(request.content)

        def extract():
            with ZipFile(f'{name}.zip', 'r') as zip:
                zip.extractall()

        if force or not os.path.exists(f'{name}.zip'):
            download()
        if os.path.exists(name):
            if force:
                rmtree(name)
            else:
                return
        
        extract()
