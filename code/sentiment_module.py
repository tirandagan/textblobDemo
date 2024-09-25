
from textblob import TextBlob

def analyze_sentiment(sentence):
    blob = TextBlob(sentence)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return polarity, subjectivity
