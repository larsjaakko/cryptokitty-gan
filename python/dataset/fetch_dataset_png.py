import requests
import json
import time
from tqdm import tqdm
from multiprocessing import Process, Queue, Pool
from pathlib import Path, PurePath, PosixPath
import os
import subprocess

from PIL import Image

import request_functions as rf
import numpy as np


raw_folder = Path.cwd() / 'data/raw'
out_folder = Path.cwd() / 'data/processed_png'

dataset_size = 150000
image_size = (128, 128)

def get_download_list():

    tqdm.write("Generating download list...")

    existing = sorted(out_folder.glob('*.png'))
    existing_ids = []

    for i, file in enumerate(existing):
        file = PurePath(file)
        existing_ids.append(file.stem)

    existing_ids = np.array(existing_ids, dtype=int)
    downloaded = len(existing_ids)

    tqdm.write("Already downloaded {} kitties! We'll get the rest now.\n\n".format(downloaded))

    id_pool = np.arange(1, 900000)
    id_pool = np.setdiff1d(id_pool, existing_ids)
    dl_list = np.random.choice(id_pool,
                                size=dataset_size-downloaded,
                                replace=False)

    return dl_list


def worker(file_id):
    """
    Each process fetches an image before converting it. It should be
    faster (and way simpler) to run the end-to-end process in parallell than
    using a queue object between a downloader and a converter functions
    """

    try:
        url = rf.get_url(file_id, ".png")
        file = rf.fetch_file(url, file_id)

        conv_return = convert(file)
        return conv_return

    except (requests.exceptions.RequestException, json.decoder.JSONDecodeError) as e:
        #tqdm.write(e)
        pass
    except Exception as e:
        #tqdm.write(e.__doc__)
        #tqdm.write(e.message)
        pass


def convert(filestr):

    """
    Converts the given path to the proper size png.
    """

    try:
        file = PurePath(filestr)
        path = Path(file)

    except Exception as e:
        #tqdm.write(e)
        #tqdm.write("Sleeping for a bit before retrying the conversion process..")
        time.sleep(10)

    output = str(out_folder / file.stem) + '.png'

    try:
        image = Image.open(path)

        # Select random number of pixels to add to the minimum bounds for cropping
        pixels = np.random.choice(np.arange(1,250))
        # The right bound only has around 83 pixels of space
        # from the inner bound, so setting that value first
        # Inner bound has coordinates 461, 181, 1917, 1637
        # size 1917-461 = 1456
        right = 1917 + np.random.choice(np.arange(np.min([pixels, 84])))
        left = right - (1456 + pixels)
        upper = 181 - np.random.choice(np.arange(np.min([pixels, 182])))
        lower = upper + (1456 + pixels)
        rotation = np.random.normal(loc=0, scale=3)

        image = image.crop((left, upper, right, lower))
        background = Image.new('RGBA', image_size, color='white')
        resized = image.resize(image_size, resample=Image.LANCZOS)
        rotated = resized.rotate(angle=rotation, resample=Image.BICUBIC)
        composite = Image.alpha_composite(background, rotated)

        # Flipping half of the images
        if np.random.randint(0, 2) == 1:
            composite = composite.transpose(method=Image.FLIP_LEFT_RIGHT)

        composite.save(output)

        path.unlink()
        return 1

    except Exception as e:
        print(e)
        path.unlink()
        return 0


def main():

    download_list = get_download_list()
    downloaded = dataset_size - len(download_list)

    # Kicking off a bunch of workers
    with Pool(8) as p:
        r = list(tqdm(p.imap(worker, download_list),
                        total=dataset_size,
                        initial=downloaded
                        ))

    p.close()
    p.join()


if __name__ == "__main__":
    main()
