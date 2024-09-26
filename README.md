
# **TextBlob Library Demo**

This demo is for week 5 of the FDU AI Class Students
The script demonstrates the key features of the TextBlob package which relies on NLTK. [Read more about TextBlob](https://textblob.readthedocs.io/en/dev/) and pay extra attention to the use of [Sentiment Analysis](https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis) for your homework assignment

## **1. Installation**
Before you start, ensure that you activate the environment and create a folder for this program outside of your **.env** folder:

```bash
cd ~
git clone https://github.com/tirandagan/textblobDemo.git
cd textblobDemo/code
```

## **2. Install Required Python Packages**
Install all the necessary packages using `pip`:
```bash
pip install textblob nltk
pip install --upgrade pip  # Upgrade pip to the latest version
```

## **3. Download NLTK Corpora**
The TextBlob library and some of your modules require additional corpora from NLTK. You can download them using the command:
```bash
python -m nltk.downloader all
```
<font color="#cE5030">**NOTE**: This above command performs an indiscrimnant download of all the corpora and requires large disk storage.</font>

---
### Note about installing corpora: ###
You should check which corpora you actually need to run your final program. Just delete the entire folder named `~/nltk_data` and install just the necessary modules with commands such as:

```bash
python -m nltk.downloader averaged_perceptron_tagger
python -m nltk.downloader punkt
python -m nltk.downloader wordnet
python -m nltk.downloader brown
```
or run the nltk downloader interactively:
```bash
python -m nltk.downloader
```
---

## **4. Test the Program**

Run the main program:
```bash
python main_program.py
```
## **5. Sample output**

```
Please enter a sentence: most of the people I meet don't know anything about pottery.

-----------------------
Tokenization:
Words: ['most', 'of', 'the', 'people', 'I', 'meet', 'do', "n't", 'know', 'anything', 'about', 'pottery']
Sentences: ["most of the people I meet don't know anything about pottery."]

-----------------------
Part-of-Speech Tagging:
most: JJS (Adjective, superlative)
of: IN (Preposition/subordinating conjunction)
the: DT (Determiner)
people: NNS (Noun, plural)
I: PRP (Personal pronoun)
meet: VBP (Verb, non-3rd person singular present)
do: VBP (Verb, non-3rd person singular present)
n't: RB (Adverb)
know: VB (Verb, base form)
anything: NN (Noun, singular or mass)
about: IN (Preposition/subordinating conjunction)
pottery: NN (Noun, singular or mass)

-----------------------
WordNet Synonyms and Definitions:
Word: most
- Synonym: most.a.01, Definition: (superlative of `many' used with count nouns and often preceded by `the') quantifier meaning the greatest in number, Examples: ['who has the most apples?', 'most people like eggs', 'most fishes have fins']
- Synonym: most.a.02, Definition: the superlative of `much' that can be used with mass nouns and is usually preceded by `the'; a quantifier meaning the greatest in amount or extent or degree, Examples: ['made the most money he could', 'what attracts the most attention?', 'made the most of a bad deal']
Word: people
- Synonym: people.n.01, Definition: (plural) any group of human beings (men or women or children) collectively, Examples: ['old people', 'there were at least 200 people in the audience']
- Synonym: citizenry.n.01, Definition: the body of citizens of a state or country, Examples: ['the Spanish people']
Word: I
- Synonym: iodine.n.01, Definition: a nonmetallic element belonging to the halogens; used especially in medicine and photography and in dyes; occurs naturally only in combination in small quantities (as in sea water or rocks), Examples: []
- Synonym: one.n.01, Definition: the smallest whole number or a numeral representing this number, Examples: ['he has the one but will need a two and three to go with it', 'they had lunch at one']
Word: meet
- Synonym: meet.n.01, Definition: a meeting at which a number of athletic contests are held, Examples: []
- Synonym: meet.v.01, Definition: come together, Examples: ["I'll probably see you at the meeting", 'How nice to see you again!']
Word: do
- Synonym: bash.n.02, Definition: an uproarious party, Examples: []
- Synonym: do.n.02, Definition: the syllable naming the first (tonic) note of any major scale in solmization, Examples: []
Word: know
- Synonym: know.n.01, Definition: the fact of being aware of information that is known to few people, Examples: ['he is always in the know']
- Synonym: know.v.01, Definition: be cognizant or aware of a fact or a specific piece of information; possess knowledge or information about, Examples: ['I know that the President lied to the people', 'I want to know who is winning the game!', "I know it's time"]
Word: about
- Synonym: about.s.01, Definition: on the move, Examples: ['up and about', 'the whole town was astir over the incident']
- Synonym: approximately.r.01, Definition: (of quantities) imprecise but fairly close to correct, Examples: ['lasted approximately an hour', 'in just about a minute', "he's about 30 years old", "I've had about all I can stand", 'we meet about once a month', 'some forty people came', 'weighs around a hundred pounds', 'roughly $3,000', 'holds 3 gallons, more or less', '20 or so people were at the party']
Word: pottery
- Synonym: pottery.n.01, Definition: ceramic ware made from clay and baked in a kiln, Examples: []
- Synonym: pottery.n.02, Definition: the craft of making earthenware, Examples: []

-----------------------
Sentiment Analysis: Polarity=0.5, Subjectivity=0.5

-----------------------
N-Grams:
1-grams: [WordList(['most']), WordList(['of']), WordList(['the']), WordList(['people']), WordList(['I']), WordList(['meet']), WordList(['do']), WordList(["n't"]), WordList(['know']), WordList(['anything']), WordList(['about']), WordList(['pottery'])]
2-grams: [WordList(['most', 'of']), WordList(['of', 'the']), WordList(['the', 'people']), WordList(['people', 'I']), WordList(['I', 'meet']), WordList(['meet', 'do']), WordList(['do', "n't"]), WordList(["n't", 'know']), WordList(['know', 'anything']), WordList(['anything', 'about']), WordList(['about', 'pottery'])]
3-grams: [WordList(['most', 'of', 'the']), WordList(['of', 'the', 'people']), WordList(['the', 'people', 'I']), WordList(['people', 'I', 'meet']), WordList(['I', 'meet', 'do']), WordList(['meet', 'do', "n't"]), WordList(['do', "n't", 'know']), WordList(["n't", 'know', 'anything']), WordList(['know', 'anything', 'about']), WordList(['anything', 'about', 'pottery'])]

-----------------------
Collocations: []

-----------------------
BLEU Score: 0.587728372510532
```

# **11. About these demos**
Here is a detailed explanation of the various demos:
### **1. Tokenization**

- **What it does**: Splits the input text into individual words (tokens) and sentences.
- **How it works**: Uses language rules to identify word and sentence boundaries.
- **How to interpret**: Understands the basic structure and components of the text, forming the foundation for more advanced analysis.
- **Why it’s important**: Tokenization enables further processing, such as part-of-speech tagging, n-grams, and sentiment analysis.

### **2. Part-of-Speech (POS) Tagging**

- **What it does**: Assigns grammatical labels (e.g., noun, verb, adjective) to each word.
- **How it works**: Uses a pre-trained model to analyze words in the context of the sentence.
- **How to interpret**: Helps understand the role and function of each word, providing insights into the sentence's grammatical structure.
- **Why it’s important**: Essential for parsing, understanding sentence structure, and extracting meaningful information like subject-object relationships.

### **3. WordNet Analysis (Synonyms and Definitions)**

- **What it does**: Finds synonyms, definitions, and examples for words using the WordNet database.
- **How it works**: Searches for word meanings and relationships based on linguistic data.
- **How to interpret**: Provides deeper understanding of word meanings and usage in different contexts.
- **Why it’s important**: Useful for applications like synonym replacement, enhancing vocabulary, and word sense disambiguation.

### **4. Sentiment Analysis**

- **What it does**: Measures the emotional tone of the text by analyzing polarity (positive/negative) and subjectivity (objective/subjective).
- **How it works**: Uses pre-trained models to score sentences based on emotional words and expressions.
- **How to interpret**:
    - **Polarity**: Ranges from -1 (negative) to 1 (positive). Indicates whether the sentiment is negative, neutral, or positive.
    - **Subjectivity**: Ranges from 0 (objective) to 1 (subjective). Shows how much personal opinion or emotion is present.
- **Why both are important**: Analyzing polarity alone might be misleading if the sentence is factual but strongly positive/negative. Combining polarity and subjectivity provides a more nuanced understanding of whether a sentiment is a factual statement or an emotional opinion.

### **5. N-Grams**

- **What it does**: Extracts contiguous sequences of words of length 'n' (e.g., unigrams, bigrams, trigrams).
- **How it works**: Identifies word sequences by sliding a window of size 'n' across the text.
- **How to interpret**: Reveals common word patterns and phrases, which can indicate topics, styles, or recurring themes.
- **Why it’s important**: Helps identify collocations, common expressions, and text patterns, valuable for applications like text generation and language modeling.

### **6. Collocations**

- **What it does**: Finds words or phrases that frequently appear together in the text.
- **How it works**: Analyzes word pairs based on frequency and statistical significance.
- **How to interpret**: Highlights fixed expressions, idioms, or phrases that convey specific meanings.
- **Why it’s important**: Identifying collocations can improve understanding of context, language nuances, and natural phrasing.

### **7. BLEU Score Calculation**

- **What it does**: Measures the similarity between machine-generated text and reference text.
- **How it works**: Compares overlapping n-grams between the two texts and calculates a score.
- **How to interpret**: Higher scores indicate greater similarity; scores range from 0 to 1.
- **Why it’s important**: Useful for evaluating the quality of text generation models, such as in machine translation or text summarization tasks.