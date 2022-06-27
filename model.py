import numpy as np
import pandas as pd
import string
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from spacy.lang.en.stop_words import STOP_WORDS
import spacy
import os 
from spacy.lang.en.examples import sentences 
#import preprocess_kgptalkie as ps
punc=string.punctuation
stopwords=list(STOP_WORDS)
nlp = spacy.load('en_core_web_sm')
doc = nlp(sentences[0])

def text_cleaner(sentence):
    doc=nlp(sentence)
    print('pass1')
    tokens=[]
    for token in doc:
        if token.lemma_!="-PRON-":
            temp=token.lemma_.lower().strip()
        else:
            temp=token.lower_
        tokens.append(temp)
    print('pass2')   
    cleaned_tokens=[]
    for token in tokens:
        if token not in stopwords and token not in punc:
            cleaned_tokens.append(token)
    print('pass3')
    return cleaned_tokens


