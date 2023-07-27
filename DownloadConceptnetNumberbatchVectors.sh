#!/bin/bash

cd linguae/data/conceptnetFiles
wget http://conceptnet.s3.amazonaws.com/precomputed-data/2016/numberbatch/19.08/mini.h5
python fromH5totxtFile.py