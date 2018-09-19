# cryptokitty-gan
Using Cryptokitties to train a GAN.

## Dataset

Dataset is created by calling the open Cryptokitties API. Images are downloaded as .png files, cropped, given a white background and resized down to 128x128 using Pillow.
The raw dataset of 150,000 cryptokitties scaled to 128x128 can be downloaded [here](https://www.dropbox.com/s/egq2q51gaj1rzjq/cryptokitties_256_png.zip?dl=0).

## GAN architecture

The employed neural network is a Tensorflow implementation of the model proposed in [Berthelot, Schumm and Metz, 2017](#references). The exact implementation used is one by [Taehoon Kim](https://github.com/carpedm20/BEGAN-tensorflow). Minor modifications were made to the original code to be more compatible with Floydhub — e.g. outputting loss metrics with JSON formatting.


## Requirements

### Building the dataset
* Python 3.6+
* Pillow
* Requests
* tqdm
* Numpy

### Tensorflow model
Refer to the [original implementation by Taehoon Kim](https://github.com/carpedm20/BEGAN-tensorflow).
## References

* [Berthelot, Schumm and Metz. BEGAN: Boundary Equilibrium Generative Adversarial Networks. arXiv preprint, 2017](https://arxiv.org/abs/1703.10717)
