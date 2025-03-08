import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download the necessary NLTK data if you haven't already
nltk.download('punkt')
nltk.download('stopwords')

# Text to process
text = """Natural Language Toolkit (NLTK) works as a powerful Python library that a wide range of tools for 
Natural Language Processing (NLP). From fundamental tasks like text pre-processing to more advanced operations 
such as semantic reasoning, NLTK provides a versatile API that caters to the diverse needs of language-related tasks."""

# Tokenize the text into words
words = word_tokenize(text)

# Get the list of English stopwords
stop_words = set(stopwords.words('english'))

# Filter out stopwords from the tokenized words
filtered_words = [word for word in words if word.lower() not in stop_words and word.isalnum()]

# Output the filtered words
print("Filtered Words:", filtered_words)
