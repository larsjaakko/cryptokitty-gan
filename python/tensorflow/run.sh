#!/bin/bash

# Creating directory for data
#mkdir /data

# Creating symlink so BEGAN code can access dataset
ln -s /floyd/input/cryptokitties /floyd/home/data

# Running job

python main.py --dataset=cryptokitties --use_gpu=True
