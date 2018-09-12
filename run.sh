#!/bin/bash
python python/tensorflow/main.py --start-epoch=0 --add-epochs=10 --save-every 1 --image-size 128
python python/tensorflow/main.py --start-epoch=0 --add-epochs=10 --train=0 --image-size 128
