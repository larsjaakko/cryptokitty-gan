#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from cairosvg import svg2png
from pathlib import Path
import os

from wand.api import library
import wand.color
from wand.image import Image

raw_folder = Path.cwd() / 'data/raw'
out_folder = Path.cwd() / 'data/processed_png'

def get_filelist():

    files = os.listdir(str(raw_folder))

    return files

def convert_to_png(files):

    for i, file in enumerate(files):

        if Path(file).suffix == '.svg':


            input = str(raw_folder / file)
            output = str(out_folder / file.replace('.svg', '.png'))

            with Image(filename=input, format='svg', height=256, width=256) as image:

                #image.sample(256, 256)
                image.format = 'jpeg'
                image.save(filename=output)
               # with wand.color.Color('transparent') as background_color:
               #     library.MagickSetBackgroundColor(image.wand,
               #                          background_color.resource)
               #
               #
               # image.read(blob=input.read(), format="svg")
               # png_image = image.make_blob("png32")

            # with open(output_filename, "wb") as out:
            #    out.write(png_image)

        else:
           continue


def resize():
    pass


def main():

    files = get_filelist()
    convert_to_png(files)

if __name__ == "__main__":
    main()
