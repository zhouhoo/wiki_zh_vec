from snakemake.remote.HTTP import RemoteProvider as HTTPRemoteProvider
import os
HTTP = HTTPRemoteProvider()

# The directory containing the data files. By default, this is "data" under
# the current directory, but it can be overridden using the
# INPUT_DATA environment variable. This will happen during testing.
DATA = os.environ.get("INPUT_DATA", "data")


RAW_WIKI_ZH_URL = "https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2"
OPENCC_JSON = "/usr/share/opencc/t2s.json"

Glove_Build ='tmp/GloVe-1.2/build'


rule all:
    input:
         DATA + "/zhwiki_extracted/AA/wiki_00",
         DATA + "/zhwiki_extracted/zh_wiki",
         DATA + "/filtered/wiki_zh_no_punc",
         DATA + "/filtered/wiki_zh_tokened",
         DATA + "/word2vec/",
         DATA + "/glove/zhs_wiki_vocab",
         DATA + "/glove/zhs_wiki_vocab",
         DATA + "/glove/zhs_wiki_cooccurence.bin",
         DATA + "/glove/zhs_wiki_shuff.bin",
         DATA + "/glove/zhs_wiki_glove.vectors"

rule clean:
    shell:
        "for subdir in zhwiki_extracted filtered word2vec glove; "
        "do echo Removing %(data)s/$subdir; "
        "rm -rf %(data)s/$subdir; done" % {'data': DATA}



# Downloaders
# ===========
rule download_wiki:
    output:
        DATA + "/raw/zhwiki-latest-pages-articles.xml.bz2"
    shell:
        "curl {RAW_WIKI_ZH_URL}> {output}"





rule extract_wiki:
    input:
        DATA + "/raw/zhwiki-latest-pages-articles.xml.bz2"
    output:
        DATA + "/zhwiki_extracted/"
    shell:
        "python3 wikiextractor/WikiExtractor.py  -b 20000M -o {output} {input}"

rule wiki_to_zh:
    input:
        wiki_data = DATA + "/zhwiki_extracted/AA/wiki_00",
        json_data = OPENCC_JSON
    output:
        DATA + "/zhwiki_extracted/zh_wiki"
    shell:
        "opencc -i {input.wiki_data} -o {output} -c {input.json_data}"


rule wiki_punctuation:
    input:
        DATA + "/zhwiki_extracted/zh_wiki"
    output:
        DATA + "/filtered/wiki_zh_no_punc"
    shell:
        "python3  -m remove_punctuation {input} {output}"

rule wiki_tokenize:
    input:
        DATA + "/filtered/wiki_zh_no_punc"
    output:
        DATA + "/filtered/wiki_zh_tokened"
    shell:
        "python3 -m wiki_token {input} {output}"

rule train_word2vec:
    input:
        DATA + "/filtered/wiki_zh_tokened"
    output:
        DATA + "/word2vec/vector"
    shell:
        "python3 -m vector_train {input} {output}"


rule train_glove_vocab:
    input:
        DATA + "/filtered/wiki_zh_tokened"
    output:
        DATA + "/glove/zhs_wiki_vocab"
    shell:
        "%(glove_bin)s/vocab_count -min-count 5 -verbose 2 < {input} > {output}"%{'glove_bin':Glove_Build}

rule train_glove_curence:
    input:
        tokened_wiki=DATA + "/filtered/wiki_zh_tokened",
        wiki_vocab = DATA + "/glove/zhs_wiki_vocab"
    output:
        DATA + "/glove/zhs_wiki_cooccurence.bin"
    shell:
        "%(glove_bin)s/cooccur -memory 4.0 -vocab-file {input.wiki_vocab}  -verbose 2 -window-size 5 < {input.tokened_wiki} > {output}"%{'glove_bin':Glove_Build}


rule train_glove_shuffle:
    input:
        DATA + "/glove/zhs_wiki_cooccurence.bin"
    output:
        DATA + "/glove/zhs_wiki_shuff.bin"
    shell:
        "%(glove_bin)s/shuffle  -memory 4.0 -verbose 2 < {input} > {output}"%{'glove_bin':Glove_Build}


rule train_glove_vector:
    input:
        shuff = DATA + "/glove/zhs_wiki_shuff.bin",
        vocab = DATA + "/glove/zhs_wiki_vocab"
    output:
        DATA + "/glove/zhs_wiki_glove.vectors"
    shell:
        "%(glove_bin)s/glove -save-file > {output} -threads 8 -input-file {input.shuff} -vocab-file {input.vocab} -x-max 10 -iter 5 -vector-size 300 -binary 2 -verbose 2"%{'glove_bin':Glove_Build}

