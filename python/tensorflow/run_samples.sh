#!/bin/bash

# Creating directory for data
mkdir -p /floyd/home/data
mkdir /floyd/home/data/logs

# Creating symlink so BEGAN code can access dataset
ln -s /floyd/input/cryptokitties /floyd/home/data
ln -s /floyd/input/logs /floyd/home/data

# Running job
python main.py --dataset=cryptokitties --load_path=cryptokitties_0915_121042 --use_gpu=True --is_train=False --split valid
