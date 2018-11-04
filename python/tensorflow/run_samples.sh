#!/bin/bash

# Creating directory for data
mkdir -p /floyd/home/data
mkdir -p /floyd/home/logs

# Creating symlink so BEGAN code can access dataset
ln -s /floyd/input/cryptokitties /floyd/home/data
#ln -s /floyd/input/cryptokitties_1007_113444 /floyd/home/logs_2
! cp -R /floyd/input/cryptokitties-test logs/cryptokitties_test

# Running job
#python main.py --dataset=cryptokitties --test_data_path=test_data --load_path=cryptokitties_1007_113444 --use_gpu=True --is_train=False --z_num=256 --gamma=0.7 --split valid
python main.py --dataset=cryptokitties --load_path=cryptokitties_test --use_gpu=True --is_train=False --z_num=256 --gamma=0.7 --split=valid
