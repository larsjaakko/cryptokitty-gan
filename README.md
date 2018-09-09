# cryptokitty-gan
Attempt at using Cryptokitties to train a GAN.

## Dataset

Dataset is created by calling the open Cryptokitties API. Images are downloaded as .png files, resized down to 256 x 256 with Pillow and given a white background.

## GAN architecture

The employed neural network is a Tensorflow implementation of the model proposed in [Berthelot, Schumm and Metz, 2017.](#references). The exact implementation used is one by [Arthur Goldberg ](https://github.com/artcg/BEGAN).

## Requirements

### Building the dataset
* Python 3.6+
* Pillow
* Requests
* tqdm
* Numpy.

### Tensorflow model
Refer to the [original implementation by Arthur Goldberg ](https://github.com/artcg/BEGAN).

## References

* [Berthelot, Schumm and Metz. BEGAN: Boundary Equilibrium Generative Adversarial Networks. arXiv preprint, 2017](https://arxiv.org/abs/1703.10717)
