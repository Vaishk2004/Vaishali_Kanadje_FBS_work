#Count the number of vowel in string
str = input("Enter string: ")

count = 0
for i in str:
    if i in "aeiouAEIOU":
        count += 1

print("No. of Vowels: ",count)