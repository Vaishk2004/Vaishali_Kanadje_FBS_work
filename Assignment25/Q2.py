import re

def date(text):
    pattern = r'\b(\d{1,2}/\d{1,2}/\d{4}|\d{1,2}-\d{1,2}-\d{4}|[A-Za-z]+\s\d{1,2},\s\d{4})\b'
    dates = re.findall(pattern, text)
    return dates

text = """
Our meetings are scheduled on 12/05/2023, 05-12-2023 and January 1, 2023.
The project started on March 15, 2022 and ended on 10/09/2023.
"""

result = date(text)
print(result)