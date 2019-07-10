
import nltk
import numpy as np 

class Corpora:
   
    def __init__(self, texts):
        self.texts = texts
   
    # build volcabulary
    
    def build_vol(self):
        vol = self.texts
        return vol