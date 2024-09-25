
from textblob import TextBlob
from nltk.translate.bleu_score import sentence_bleu

def calculate_bleu_score(sentence):
    reference = [sentence.split()]
    hypothesis = TextBlob(sentence).words[:len(reference[0])]
    bleu_score = sentence_bleu(reference, hypothesis)
    return bleu_score
