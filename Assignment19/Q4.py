# Remove all vowels in string (take input from user)
str1 = input("Enter string: ")

vowel = 'aeiouAEIOU'

result = ''.join([s for s in str1 if s not in vowel])


print("Strinf after remove vowels: ",result)