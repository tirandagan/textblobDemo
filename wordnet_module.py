
from textblob import TextBlob
from nltk.corpus import wordnet as wn

def wordnet_analysis(sentence):
    blob = TextBlob(sentence)
    word_definitions = {}
    for word in blob.words:
        synsets = wn.synsets(word)
        if synsets:
            word_definitions[word] = [(synset.name(), synset.definition(), synset.examples()) for synset in synsets[:2]]
    return word_definitions
