
from tokenization_module import tokenize_sentence
from pos_tagging_module import pos_tagging
from wordnet_module import wordnet_analysis
from sentiment_module import analyze_sentiment
from ngram_module import generate_ngrams
from collocations_module import find_collocations
from bleu_module import calculate_bleu_score

def main():
    sentence = input("Please enter a sentence: ").strip()

    # Tokenization
    print("\n-----------------------")
    words, sentences = tokenize_sentence(sentence)
    print("Tokenization:")
    print(f"Words: {words}")
    print(f"Sentences: {sentences}")

    # Part-of-Speech Tagging
    print("\n-----------------------")
    pos_tags = pos_tagging(sentence)
    print("Part-of-Speech Tagging:")
    for word, tag, description in pos_tags:
        print(f"{word}: {tag} ({description})")

    # WordNet Analysis
    print("\n-----------------------")
    wordnet_results = wordnet_analysis(sentence)
    print("WordNet Synonyms and Definitions:")
    for word, details in wordnet_results.items():
        print(f"Word: {word}")
        for syn_name, definition, examples in details:
            print(f"- Synonym: {syn_name}, Definition: {definition}, Examples: {examples}")

    # Sentiment Analysis
    print("\n-----------------------")
    polarity, subjectivity = analyze_sentiment(sentence)
    print(f"Sentiment Analysis: Polarity={polarity}, Subjectivity={subjectivity}")

    # N-Grams
    print("\n-----------------------")
    ngrams = generate_ngrams(sentence)
    print("N-Grams:")
    for n, grams in ngrams.items():
        print(f"{n}: {grams}")

    # Collocations
    print("\n-----------------------")
    collocations = find_collocations(sentence)
    print(f"Collocations: {collocations}")

    # BLEU Score
    print("\n-----------------------")
    bleu_score = calculate_bleu_score(sentence)
    print(f"BLEU Score: {bleu_score}")

if __name__ == "__main__":
    main()
