import request_functions as rf
import numpy as np
import requests
import json
import time
from tqdm import tqdm

from multiprocessing import Process, Queue, Pool

from pathlib import Path, PurePath, PosixPath
import os

import subprocess

raw_folder = Path.cwd() / 'data/raw'
out_folder = Path.cwd() / 'data/processed_png'

dataset_size = 150000

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

    #tqdm.write('Fetching kitty #{}'.format(file_id))

    try:
        url = rf.get_url(file_id)
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
    Converts the given path to png.
    """

    try:
        file = PurePath(filestr)
        path = Path(file)

    except Exception as e:
        #tqdm.write(e)
        #tqdm.write("Sleeping for a bit before retrying the conversion process..")
        time.sleep(10)

    if file.suffix == '.png':
        #tqdm.write('Kitty #{} was a .png! Deleting this troll kitten.'.format(file.stem))
        path.unlink()

        return 0

    input = filestr
    output = str(out_folder / file.stem) + '.png'

    inkscape_string = 'inkscape -z {} -e {} -w 256 -b "#ffffff"'.format(input, output)

    if file.suffix == '.svg':

        try:
            subprocess.run(inkscape_string, shell=True, check=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
            #tqdm.write('Converted kitty #{}!'.format(file.stem))

        except Exception as e:
            pass
            #tqdm.write("Skipped conversion of kitty #{} for some error: {}".format(file.stem, e.__doc__))

        path.unlink()

        return 1


def main():

    download_list = get_download_list()
    downloaded = dataset_size - len(download_list)

    with Pool(4) as p:

        r = list(tqdm(p.imap(worker, download_list),
                        total=dataset_size,
                        initial=downloaded
                        ))

    p.close()
    p.join()


if __name__ == "__main__":
    main()
