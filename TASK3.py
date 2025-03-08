import string

# Original text
text = "Let’s eat, Grandma! Grandma, Let’s eat! Silvia, Are you free tomorrow? Yes, I’m free on Saturday."

# Convert text to lowercase
text_lower = text.lower()

# Remove punctuation
translator = str.maketrans('', '', string.punctuation)
text_no_punctuation = text_lower.translate(translator)

# Output the cleaned text
print(text_no_punctuation)
