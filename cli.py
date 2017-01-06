import click
from remove_punctuation import remove_punctuation
from wiki_token import cut_words

from vector_train import word2vec_train
from increatement_train import  word2vec_increment_train



@click.group()
def cli():
    pass


@cli.command(name='wiki_remove_punctuation')
@click.argument('input', type=click.Path(readable=True, dir_okay=False))
@click.argument('output', type=click.Path(writable=True, dir_okay=False))
def run_wiki_remove_punctuation(input, output):
    remove_punctuation(input,output)


@cli.command(name='wiki_tokenize')
@click.argument('no_punctuation_wiki_zh', type=click.Path(readable=True, dir_okay=False))
@click.argument('tokened_wiki_zh', type=click.Path(writable=True, dir_okay=False))
def wiki_tokenize(no_punctuation_wiki_zh,tokened_wiki_zh):
    cut_words(no_punctuation_wiki_zh,tokened_wiki_zh)


@cli.command(name='train_word2vec')
@click.argument('tokened_wiki_zh', type=click.Path(readable=True, dir_okay=False))
@click.argument('vector_file', type=click.Path(writable=True, dir_okay=False))
def train_word2vec(tokened_wiki_zh, vector_file):
    word2vec_train(tokened_wiki_zh, vector_file)


@cli.command(name='increment_train_word2vec')
@click.argument('new_corpus', type=click.Path(readable=True, dir_okay=False))
@click.argument('model_file', type=click.Path(readable=True, dir_okay=False))
@click.argument('vector_file', type=click.Path(writable=True, dir_okay=False))
def increment_train_word2vec(new_corpus, model_file, vector_file):
    word2vec_increment_train(new_corpus, model_file, vector_file)


