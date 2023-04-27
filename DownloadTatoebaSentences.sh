#!/bin/bash

cd linguae/data/tatoebaFiles
wget https://downloads.tatoeba.org/exports/sentences.tar.bz2
tar -xf sentences.tar.bz2
rm sentences.tar.bz2 
