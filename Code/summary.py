import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import defaultdict

nltk.download('punkt')
nltk.download('stopwords')

text = """Your input paragraph goes here. Replace this text with any content 
you want to summarize. This program will extract the most important sentence 
based on keyword frequency."""

stop_words = set(stopwords.words('english'))

words = word_tokenize(text.lower())

freq = defaultdict(int)
for word in words:
    if word.isalnum() and word not in stop_words:
        freq[word] += 1

sentences = sent_tokenize(text)

sentence_scores = {}
for sent in sentences:
    for word in word_tokenize(sent.lower()):
        if word in freq:
            sentence_scores[sent] = sentence_scores.get(sent, 0) + freq[word]

best_sentence = max(sentence_scores, key=sentence_scores.get)

print("Most Important Sentence:\n")
print(best_sentence)