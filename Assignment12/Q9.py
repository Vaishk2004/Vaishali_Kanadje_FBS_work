#Python program to calculate the number of words and number of characters in string
str = input("Enter string: ")

word = 1
chara = 0

for i in str:
    if i.isalpha():
        chara += 1
    elif i.isspace():
        word += 1

print("No. of Words: ",word)
print("No. of Characters: ",chara)