#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import shutil
from pathlib import Path

from urllib.parse import urlparse

import os
import time



def get_url(id, format=None):

    """
    Takes a kitty ID as argument, and parses the json blob to return the
    url to the .svg file.
    """

    url = 'http://api.cryptokitties.co/kitties/' + str(id)

    r = requests.get(url)

    blob = r.json()
    img_url = blob.get('image_url_cdn')

    path = urlparse(img_url).path
    ext = os.path.splitext(path)[1]

    if ext == '.png':
         tqdm.write('PNGPNG')
         raise ValueError('This is one of them special kitties. Try the next one')

    if format:
        img_url = img_url.replace('.svg', format)

    return img_url


def fetch_file(url, id):
    """
    Takes a kitty ID and its .svg url as arguments. Downloads the file and
    returns the file path for further processing.
    """

    data_folder = Path.cwd() / 'data/raw'
    filename = os.path.basename(url)
    path = data_folder / filename

    r = requests.get(url, stream=True)

    with open(str(path), 'wb') as out_file:
        shutil.copyfileobj(r.raw, out_file)

    return path

def cooldown():

    time.sleep(5)
