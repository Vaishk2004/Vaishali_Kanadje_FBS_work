import re
from collections import Counter

def frequency(text):
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = Counter(words)
    return word_count

text = "Python is great, and Python is easy to learn. Learn Python!"
result = frequency(text)
print(result)
