from glob import glob
from pathlib import Path, PosixPath
import numpy as np
import h5py
from tqdm import tqdm
from scipy.misc import imread, imresize

in_folder = Path.cwd() / 'data/processed_png'
out_folder = Path.cwd() / 'data/processed_h5'
filenames = sorted(in_folder.glob('*.png'))

w, h = 256, 256  # Change this if you wish to use larger images
data = np.zeros((len(filenames), w * h * 3), dtype = np.uint8)

# This preprocessing is appriate for CelebA but should be adapted
# (or removed entirely) for other datasets.

def get_image(image_path, w=64, h=64):
    im = imread(image_path).astype(np.float)[:,:,:3] #Dropping the alpha channel
    orig_h, orig_w = im.shape[:2]
    if orig_h != h:
        new_h = int(orig_h * w / orig_w)
        im = imresize(im, (new_h, w))
        margin = int(round((new_h - h)/2))
        return im[margin:margin+h]
    else:
        return im

for n, fname in tqdm(enumerate(filenames), total=len(filenames)):
    image = get_image(fname, w, h)
    data[n] = image.flatten()

out_file = 'kitties_' + str(w) + '.h5'
out_file = out_folder / out_file

with h5py.File(out_file, 'w') as f:
    f.create_dataset("images", data=data)
