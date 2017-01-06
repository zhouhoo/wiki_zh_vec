
from gensim.models import word2vec, Word2Vec


def word2vec_increment_train(input_file,model_file, output_file):
    new_sentences = word2vec.LineSentence(input_file)
    model = Word2Vec.load(model_file)
    model.train(new_sentences)
    model.save(output_file)
    model.save_word2vec_format(output_file + '.vector', binary=True)


if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help=' sentences of input')
    parser.add_argument('model', help='model   of input')
    parser.add_argument('output', help='vector file to output to')
    args = parser.parse_args()
    word2vec_increment_train(args.input, args.model, args.output)