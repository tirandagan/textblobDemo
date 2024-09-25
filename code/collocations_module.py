
from textblob import TextBlob

def find_collocations(sentence):
    blob = TextBlob(sentence)
    return blob.noun_phrases
