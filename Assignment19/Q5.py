# find all of the word in string that are less than 5 letter (take input from user)

str1 = input("Enter string: ")
words = str1.split()

result = [word for word in words if len(word) < 5]

print("Words in string that are less than 5 letter: ",result)