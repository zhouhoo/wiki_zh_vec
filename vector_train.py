
import multiprocessing
from gensim.models import word2vec, Word2Vec


def word2vec_train(input_file, output_file):
    sentences = word2vec.LineSentence(input_file)
    model = Word2Vec(sentences, size=300, min_count=10, sg=0, workers=multiprocessing.cpu_count())
    model.save(output_file)
    model.save_word2vec_format(output_file + '.vector', binary=True)


if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='corpus  of input')
    parser.add_argument('output', help='vector file to output to')
    args = parser.parse_args()
    word2vec_train(args.input, args.output)