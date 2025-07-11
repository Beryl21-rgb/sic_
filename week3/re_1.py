import re

data = ["Hello123", "A@B#C", "Clean_text", "X Y Z"]

# Remove all non-alphabetic characters
cleaned = list(map(lambda s: re.sub(r'[^a-zA-Z]', '#', s), data))
print(cleaned)  # ['Hello', 'ABC', 'Cleantext', 'XYZ']


emails = ["alice@gmail.com", "bob@yahoo.com", "user@outlook.com"]

# Extract domain using regex
domains = list(map(lambda s: re.search(r'@(\w+)\.com', s).group(1), emails))
print(domains)  # ['gmail', 'yahoo', 'outlook']

words = ["apple", "banana", "orange", "grape", "umbrella"]

# Capitalize if starts with a vowel
vowel_caps = list(map(lambda w: re.sub(r'^[aeiou]', lambda m: m.group(0).upper(), w), words))
print(vowel_caps)  # ['Apple', 'banana', 'Orange', 'grape', 'Umbrella']

texts = ["Hello   World", "Python    is great", "No extra   spaces please"]

# Normalize spaces
normalized = list(map(lambda t: re.sub(r'\s+', ' ', t), texts))
print(normalized)  # ['Hello World', 'Python is great', 'No extra spaces please']