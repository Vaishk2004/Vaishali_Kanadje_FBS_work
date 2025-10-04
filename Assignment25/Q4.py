import re

def extract_urls(text):
    pattern = r'(https?://[^\s]+|www\.[^\s]+)'
    urls = re.findall(pattern, text)
    return urls

text = """
Check out my website at https://www.example.com and our blog at http://blog.example.org.
You can also visit www.openai.com for more information.
"""
result = extract_urls(text)
print(result)