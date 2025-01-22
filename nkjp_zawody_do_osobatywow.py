# -*- coding: utf-8 -*-
"""nkjp_zawody do osobatywow

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MvwO5a7FWSmZPUSXQxUZkRO5sExA-sy3
"""

import nltk
import os
import re
import tempfile
import spacy
import random
import json
import datetime
from nltk.corpus.reader.nkjp import NKJPCorpusReader

#from google.colab import drive
#drive.mount('/content/drive')

class XML_Tool:
    """
    Helper class creating xml file to one without references to nkjp: namespace.
    That's needed because the XMLCorpusView assumes that one can find short substrings
    of XML that are valid XML, which is not true if a namespace is declared at top level
    """

    def __init__(self, root, filename):
        self.read_file = os.path.join(root, filename)
        self.write_file = tempfile.NamedTemporaryFile(delete=False, mode='w+t')

    def build_preprocessed_file(self):
        try:
            fr = open(self.read_file)
            fw = self.write_file
            line = " "
            while len(line):
                line = fr.readline()
                x = re.split(r"nkjp:[^ ]* ", line)  # in all files
                ret = " ".join(x)
                x = re.split("<nkjp:paren>", ret)  # in ann_segmentation.xml
                ret = " ".join(x)
                x = re.split("</nkjp:paren>", ret)  # in ann_segmentation.xml
                ret = " ".join(x)
                x = re.split("<choice>", ret)  # in ann_segmentation.xml
                ret = " ".join(x)
                x = re.split("</choice>", ret)  # in ann_segmentation.xml
                ret = " ".join(x)
                fw.write(ret)
            fr.close()
            fw.close()
            return self.write_file.name
        except Exception as e:
            self.remove_preprocessed_file()
            raise Exception from e

    def remove_preprocessed_file(self):
        os.remove(self.write_file.name)

nltk.corpus.reader.nkjp.XML_Tool = XML_Tool

#nltk.download('punkt')
__dirname__ = os.path.dirname(__file__)
corpus_root = __dirname__ + '/NKJP-PodkorpusMilionowy'
fileids = [f.path for f in os.scandir(corpus_root) if f.is_dir()]



corpus = NKJPCorpusReader(corpus_root, fileids)

#corpus_texts = corpus.raw()

corpus_list = corpus.raw()
corpus_sample = random.sample(corpus_list,3)

nlp = spacy.load('pl_core_news_lg')

def preprocess(texts):        
    start_time = datetime.datetime.now()

    counter = 0
    total = len(texts)
    result = []
    for text in texts:
        counter += 1
        elapsed_time = datetime.datetime.now() - start_time

        print(f'{counter}/{total}\telapsed time: {elapsed_time.total_seconds()}s\t avg time: {elapsed_time.total_seconds()/counter}s')

        result_text = {}
        doc = nlp(text)
        result_text['raw_text'] = text
        result_text['sents'] = []
        for sentence in doc.sents:
            result_sent = {}
            result_sent['raw_sentence'] = sentence.text
            result_sent['tokens'] = []
            for token in sentence:
                result_token = {}
                result_token['pos'] = token.tag_
                result_token['text'] = token.text
                result_token['lemma'] = token.lemma_
                result_sent['tokens'].append(result_token)
            result_text['sents'].append(result_sent)
        result.append(result_text)
    return result

corpus_preprocessed = preprocess(corpus_list)

to_file = {'corpus':corpus_preprocessed}
with open('corpus.json', 'w', encoding='utf-8') as f:
    json.dump(to_file, f, ensure_ascii=False, indent=4)

