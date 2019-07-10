import numpy as np 
import pandas as pd 



path = 'data/train.tsv'


def pre_process(path):
    raw = pd.read_csv(path, sep="\t")
    train = np.array(raw)
    pid = train[:,0]
    sid = train[:,1]
    sentences = train[:,2]
    targets = train[:,3]
    return pid,sid, sentences, targets
