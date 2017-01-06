
"""
@autor: june
@date :
"""

import re
import io


def remove_punctuation(input_file, output_file):
    multi_version = re.compile('-\{.*?(zh-hans|zh-cn):([^;]*?)(;.*?)?\}-')
    punctuation = re.compile(u"[-~!@#$%^&*()_+`=\[\]\\\{\}\"|;':,./<>?·！@#￥%……&*（）——+【】、；‘：“”，。、《》？「『」』]")
    with io.open(output_file, mode = 'w', encoding = 'utf-8') as outfile:
        with io.open(input_file, mode = 'r', encoding ='utf-8') as infile:
            for line in infile:
                line = multi_version.sub('\2', line)
                line = punctuation.sub('', line)
                outfile.write(line)


if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='raw wiki data of input')
    parser.add_argument('output', help='punctuationed data to output to')
    args = parser.parse_args()
    remove_punctuation(args.input, args.output)

