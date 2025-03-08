import re

# Given text
text = """@@Natural Language Processing (NLP)!!! is a field of AI that focuses on ... enabling computers to understand, interpret, & generate human language.
NLP includes tasks like **tokenization, lemmatization,** && sentiment analysis.
It helps in applications such as chatbots, machine translation, and voice assistants!!!
However, cleaning text—removing extra spaces, punctuations, && special $$$ characters—is crucial.
Without preprocessing, NLP models may not perform accurately !!!
So, can you clean this messy text & make it structured???"""

# Step 1: Remove special characters (keeping only alphanumeric characters and spaces)
cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

# Step 2: Remove extra whitespaces (replace multiple spaces with a single space)
cleaned_text = re.sub(r'\s+', ' ', cleaned_text)

# Step 3: Remove leading and trailing spaces
cleaned_text = cleaned_text.strip()

# Output the cleaned text
print(cleaned_text)

