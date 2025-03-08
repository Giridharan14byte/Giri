import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('wordnet')

# Input text
text = """The researchers are analyzing various datasets to study the effects of automation. 
They observed that automated systems perform tasks more efficiently than humans. 
Many industries have been adopting AI-driven solutions to improve productivity. 
Running complex algorithms helps in predicting future trends accurately. 
Several companies are investing in developing smarter and more adaptive models. 
Data scientists continuously refine their models to achieve better performance. 
The advancements in technology have transformed the way businesses operate."""

# Step 1: Tokenize the text
words = word_tokenize(text)

# Step 2: Apply stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]

# Step 3: Apply lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word, pos='v') for word in words]  # 'v' for verb, could also be 'n' for noun

# Print results
print("Original Words:")
print(words)

print("\nStemmed Words:")
print(stemmed_words)

print("\nLemmatized Words:")
print(lemmatized_words)
