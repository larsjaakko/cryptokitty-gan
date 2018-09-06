import request_functions as rf
import numpy as np
import requests
import json
import time

from multiprocessing import Process, Queue

from pathlib import Path, PurePath, PosixPath
import os

import subprocess

raw_folder = Path.cwd() / 'data/raw'
out_folder = Path.cwd() / 'data/processed_png'

dataset_size = 500000

def fetcher(q):
    """
    Fetches images to be consumed and waits for the consumer
    to finish processing
    """
    downloaded = 0
    id_list = np.arange(900000)

    while downloaded <= dataset_size:

        next_id = np.random.choice(id_list, replace=False)

        print('Download #{}:\tFetching kitty #{}'.format(downloaded+1, next_id))

        try:
            url = rf.get_url(next_id)
            file = rf.fetch_file(url, next_id)
            downloaded += 1
            q.put(file)

        except (requests.exceptions.RequestException, json.decoder.JSONDecodeError) as e:
            print(e)
            continue
        except Exception as e:
            print(e.__doc__)
            print(e.message)
            continue


    if downloaded > dataset_size:
        q.put(-1)


def converter(q):

    """
    Consumes file list and converts them using the inkscape
    command line interface
    """
    while True:

        filestr = q.get()

        if filestr == -1:
            print("OK, we're done here!")
            break

        try:
            file = PurePath(filestr)
            path = Path(file)

        except TypeError as e:
            print(e)
            print("Sleeping for a bit before retrying the convert process..")

            time.sleep(10)
            continue

        if file.suffix == '.png':
            print('Kitty #{} was a .png! Deleting this troll kitten.'.format(file.stem))
            path.unlink()
            continue

        input = filestr
        output = str(out_folder / file.stem) + '.png'

        inkscape_string = 'inkscape -z {} -e {} -w 256 -b "#ffffff"'.format(input, output)

        try:
            subprocess.run(inkscape_string, shell=True, check=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)

            print('Converted kitty #{}!'.format(file.stem))

        except Exception as e:

            print("Skipped conversion of kitty #{} for some error".format(file.stem))
            print(e.__doc__)

        #path.unlink()


def main():

    q = Queue()

    fetch_process = Process(target=fetcher, args=(q,))
    convert_process = Process(target=converter, args=(q,))

    fetch_process.start()
    convert_process.start()

    q.close()
    q.join_thread()

    fetch_process.join()
    convert_process.join()

if __name__ == "__main__":
    main()
