#!/usr/bin/env bash

# install opencc and glove
mkdir tmp && cd tmp
git clone https://github.com/BYVoid/OpenCC.git
wget http://www-nlp.stanford.edu/software/GloVe-1.2.zip
wget https://github.com/alexandres/lexvec/releases/download/v1.0.1/lexvec_v1.0.1_linux_amd64.tar.gz
unzip GloVe-1.2.zip
tar zxvf lexvec_v1.0.1_linux_amd64.tar.gz


cd OpenCC && make && make install
cd ../Glove-1.2 && make





