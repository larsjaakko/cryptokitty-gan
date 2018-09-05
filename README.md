# cryptokitty-gan
Attempt at using Cryptokitties to train a GAN.

Used Anaconda, so requirements file will be an ungodly mess.

## Dataset

Dataset is created by calling the open Cryptokitties API. Images are served as .svg files, which are then converted to .png files using Inkscape's command line tool. Cairosvg and ImageMagick + wand fail to read and/or convert the .svg files properly. Inkscape, although a clunky behemoth compared to a simple python library, does the task admirably well.

Images are resized down to 256 x 256, with a white background.
