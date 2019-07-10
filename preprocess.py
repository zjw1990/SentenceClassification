import nltk
import numpy as np 
import pandas as pd 

train_raw = pd.read_csv('/media/jzhao1/498032e5-c16b-4e25-b7b7-5186838340e2/data/Classification data/train.tsv', sep="\t")
test_raw = pd.read_csv('/media/jzhao1/498032e5-c16b-4e25-b7b7-5186838340e2/data/Classification data/test.tsv', sep="\t")

train = np.array(train_raw)
test = np.array(test_raw)

sentences_train = train[:,2]
target_train = train[:,3]


class Preprocess:

    def __init__(self, path):
        return

    def pre_process(data):
        return