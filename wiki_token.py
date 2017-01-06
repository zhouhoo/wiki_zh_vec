import io
import jieba


def cut_words(input_file, output_file):
    count = 0
    with io.open(output_file, mode = 'w', encoding = 'utf-8') as outfile:
        with io.open(input_file, mode = 'r', encoding = 'utf-8') as infile:
            for line in infile:
                line = line.strip()
                if len(line) < 1:  # empty line
                    continue
                if line.startswith('doc'): # start or end of a passage
                    if line == 'doc': # end of a passage
                        outfile.write(u'\n')
                        count = count + 1
                        if(count % 1000 == 0):
                            print('%s articles were finished.......' %count)
                    continue
                for word in jieba.cut(line):
                    outfile.write(word + ' ')
    print('%s articles were finished.......' %count)


if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='punctuationed wiki  of input')
    parser.add_argument('output', help='tokened wiki file to output to')
    args = parser.parse_args()
    cut_words(args.input, args.output)