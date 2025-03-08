import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Sample text
text = "Natural Language Toolkit (NLTK) is one of the largest Python libraries for performing various Natural Language Processing tasks. From rudimentary tasks such as text pre-processing to tasks like vectorized representation of text – NLTK’s API has covered everything."

# Tokenize into sentences
sentences = sent_tokenize(text)

# Tokenize into words
words = word_tokenize(text)

# Print the results
print("Sentences Tokenized:")
print(sentences)

print("\nWords Tokenized:")
print(words)
