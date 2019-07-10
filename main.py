
import numpy as np 
import pandas as pd 
from preprocess import pre_process
from sentence import Corpora
import nltk
def main():
    
    
    pids, sids, texts, targets = pre_process('data/train.tsv')

    corp = Corpora(texts)
    vol = corp.build_vol()
    
    for i in vol[:10]:
        print(nltk.word_tokenize(i))




if __name__ == "__main__":
    main()



