#!/usr/bin/env bash

# install opencc and glove
mkdir tmp && cd tmp
git clone https://github.com/BYVoid/OpenCC.git
wget http://www-nlp.stanford.edu/software/GloVe-1.2.zip
unzip GloVe-1.2.zip


cd OpenCC && make && make install
cd ../Glove-1.2 && make





