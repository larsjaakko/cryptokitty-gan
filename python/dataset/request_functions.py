#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import shutil
from pathlib import Path
from urllib.parse import urlparse
import os
import time

def get_url(id):

    url = 'http://api.cryptokitties.co/kitties/' + str(id)

    r = requests.get(url)

    blob = r.json()
    img_url = blob.get('image_url')

    return img_url


def fetch_file(url, id):

    data_folder = Path.cwd() / 'data/raw'
    filename = os.path.basename(url)
    path = data_folder / filename

    r = requests.get(url, stream=True)

    with open(str(path), 'wb') as out_file:
        shutil.copyfileobj(r.raw, out_file)

    return path

def cooldown():

    time.sleep(5)
