# cryptokitty-gan
Attempt at using Cryptokitties to train a GAN.

## Dataset

Dataset is created by calling the open Cryptokitties API. Images are downloaded as .png files, resized down to 256 x 256 with Pillow and given a white background.

## Requirements
Pillow, Requests, tqdm, Numpy. For the tensorflow part, refer to the [original implementation by Taehoon Kim](https://github.com/carpedm20/DCGAN-tensorflow).
