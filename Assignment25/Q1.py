import re

def text(sentence,forbidden_word):
    pattern = '|'.join(forbidden_word)
    text = re.sub(pattern, lambda m: '*' * len(m.group()), sentence, flags=re.IGNORECASE)
    return text

sentence = "Python is amazing but Java is not that bad."
forbidden_words = ["Python", "Java"]

result = text(sentence, forbidden_words)
print(result)