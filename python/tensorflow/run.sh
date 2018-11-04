#!/bin/bash

# Creating directory for data
# mkdir -p /floyd/home/data/logs
mkdir -p /floyd/home/logs

# Creating symlink so BEGAN code can access dataset
ln -s /floyd/input/cryptokitties /floyd/home/data
! cp -R /floyd/input/cryptokitties-test logs/cryptokitties_test

# Running job

#python main.py --dataset=cryptokitties --d_lr=0.00004 --g_lr=0.00004 --max_step=20000 --use_gpu=True --lr_update_step=75000
#python main.py --dataset=cryptokitties --d_lr=0.00002 --g_lr=0.00002 --conv_hidden_num=64 --max_step=300000 --use_gpu=True
#python main.py --dataset=cryptokitties --d_lr=0.00004 --g_lr=0.00004 --z_num=128 --max_step=30000 --use_gpu=True
#python main.py --dataset=cryptokitties --d_lr=0.00006 --g_lr=0.00004 --max_step=30000 --use_gpu=True
#59
#python main.py --dataset=cryptokitties --d_lr=0.00001 --g_lr=0.00001 --lr_lower_boundary=0.000001 --max_step=50000 --use_gpu=True
#61
#python main.py --dataset=cryptokitties --d_lr=0.00002 --g_lr=0.00002 --lr_lower_boundary=0.000001 --max_step=50000 --use_gpu=True
#62
#python main.py --dataset=cryptokitties --d_lr=0.0000095 --g_lr=0.0000095 --lr_lower_boundary=0.0000001 --max_step=500000 --use_gpu=True
#63
#python main.py --dataset=cryptokitties --d_lr=0.00004 --g_lr=0.00004 --lr_lower_boundary=0.00001 --z_num=256 --max_step=50000 --use_gpu=True
#64
#python main.py --dataset=cryptokitties --d_lr=0.00002 --g_lr=0.00004 --lr_lower_boundary=0.00001 --max_step=50000 --use_gpu=True --num_log_samples=6
#65
#python main.py --dataset=cryptokitties --d_lr=0.000015 --g_lr=0.00004 --lr_lower_boundary=0.00001 --z_num=256 --max_step=50000 --use_gpu=True --num_log_samples=6
#66
#python main.py --dataset=cryptokitties --d_lr=0.000015 --g_lr=0.000045 --lr_lower_boundary=0.00001 --max_step=50000 --use_gpu=True --num_log_samples=6
#67
#python main.py --dataset=cryptokitties --d_lr=0.00002 --g_lr=0.00005 --lr_lower_boundary=0.00001 --max_step=50000 --use_gpu=True
#68
#python main.py --dataset=cryptokitties --d_lr=0.000015 --g_lr=0.00006 --lr_lower_boundary=0.00001 --z_num=256 --max_step=50000 --use_gpu=True --num_log_samples=6
#69
#python main.py --dataset=cryptokitties --d_lr=0.000015 --g_lr=0.00006 --lr_lower_boundary=0.00001 --z_num=256 --max_step=50000 --use_gpu=True --gamma=0.7
#71
#python main.py --dataset=cryptokitties --d_lr=0.00002 --g_lr=0.00008 --lr_lower_boundary=0.00001 --max_step=25000 --use_gpu=True --input_scale_size=128
#74
#python main.py --dataset=cryptokitties --d_lr=0.000015 --g_lr=0.00008 --lr_lower_boundary=0.00001 --max_step=35000 --use_gpu=True --gamma=0.7
#75
#python main.py --dataset=cryptokitties --d_lr=0.00001 --g_lr=0.00008 --lr_lower_boundary=0.000005 --max_step=35000 --use_gpu=True --gamma=0.7
#76 - based on 69
#python main.py --dataset=cryptokitties --d_lr=0.000015 --g_lr=0.00006 --lr_lower_boundary=0.00001 --z_num=256 --max_step=250000 --use_gpu=True --gamma=0.7
#77
#python main.py --dataset=cryptokitties --max_step=25000 --use_gpu=True --input_scale_size=128
#78
#python main.py --dataset=cryptokitties --d_lr=0.000015 --g_lr=0.00006 --lr_lower_boundary=0.00001 --z_num=256 --max_step=30000 --use_gpu=True --gamma=0.7 --input_scale_size=128
#82
#python main.py --dataset=cryptokitties --d_lr=0.00006 --g_lr=0.00006 --lr_lower_boundary=0.00001 --conv_hidden_num=64 --max_step=30000 --use_gpu=True --gamma=0.7 --input_scale_size=128
#83
#python main.py --dataset=cryptokitties --d_lr=0.00003 --lr_lower_boundary=0.00001 --z_num=256 --max_step=250000 --use_gpu=True --gamma=0.7
python main.py --dataset=cryptokitties --load_path=cryptokitties_test --d_lr=0.000015 --g_lr=0.00006 --lr_lower_boundary=0.00001 --z_num=256 --max_step=250000 --use_gpu=True --gamma=0.7
