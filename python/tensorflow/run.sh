#!/bin/bash

# Creating directory for data
mkdir /floyd/home/data

# Creating symlink so BEGAN code can access dataset
ln -s /floyd/input/cryptokitties /floyd/home/data

# Running job

#python main.py --dataset=cryptokitties --d_lr=0.00004 --g_lr=0.00004 --max_step=20000 --use_gpu=True --lr_update_step=75000
python main.py --dataset=cryptokitties --d_lr=0.00004 --g_lr=0.00004 --max_step=100000 --use_gpu=True
