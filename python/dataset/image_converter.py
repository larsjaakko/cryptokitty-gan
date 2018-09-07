#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path, PurePath, PosixPath
import os

import subprocess

raw_folder = Path.cwd() / 'data/raw'
out_folder = Path.cwd() / 'data/processed_png'

def get_filelist():

    files = sorted(raw_folder.glob('*.svg'))

    return files

def convert_to_png(files):

    for i, file in enumerate(files):

        file = PurePath(file)

        input = str(file)
        output = str(out_folder / file.stem) + '.png'

        inkscape_string = 'inkscape -z {} -e {} -w 256 -b "#ffffff"'.format(input, output)

        try:

            subprocess.run(inkscape_string, shell=True, check=True)
            path = Path(file)
            path.unlink()

        except Exception as e:

            print("Skipped {} for some error: {}".format(input, e))


def resize():
    pass


def main():

    files = get_filelist()
    convert_to_png(files)

if __name__ == "__main__":
    main()
