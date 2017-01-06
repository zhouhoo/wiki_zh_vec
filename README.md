# wiki_zh_vec

a tool for train Chinese wiki corpus for word embeddings using word2vec and glove

Installing and building wiki_zh_vec:

1. run require_install.sh to install required software.

2. install the pacakage: python3 setup.py install

3. run the script to complete building and get the vector file: snakemake -j 8 --resources 'ram=16' all

note:

1. if you have alreay done steps of Snakefile by yourself before using this pacakage, you can edit  it and comment steps you do not need.

2. my environment is ubuntu14.04&python3.5 with anaconda env & 16G . so you may need to edit Snakefile to suit your own case. 

3. the result vector file is located in data folder.
