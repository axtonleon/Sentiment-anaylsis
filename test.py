from spacy.lang.en.stop_words import STOP_WORDS
import spacy
import os 
from spacy.lang.en.examples import sentences 
stopwords=list(STOP_WORDS)
nlp = spacy.load('en_core_web_sm')
doc = nlp(sentences[0])