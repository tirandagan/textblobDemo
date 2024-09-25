
from textblob import TextBlob

def generate_ngrams(sentence, n=3):
    blob = TextBlob(sentence)
    ngrams_output = {}
    for i in range(1, n+1):
        ngrams_output[f"{i}-grams"] = list(blob.ngrams(i))
    return ngrams_output
