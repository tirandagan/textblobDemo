
from textblob import TextBlob

def tokenize_sentence(sentence):
    blob = TextBlob(sentence)
    words = blob.words
    sentences = [str(s) for s in blob.sentences]
    return words, sentences
