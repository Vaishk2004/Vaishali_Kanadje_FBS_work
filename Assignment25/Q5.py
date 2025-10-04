import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False
    
emails = [
    "student@example.com",
    "hello.world@domain.org",
    "invalid@com",
    "user@@example.com",
    "my_email123@gmail.co.in"
]

for e in emails:
    print(e, ":", validate_email(e))