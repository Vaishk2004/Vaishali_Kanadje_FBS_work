# use dictionary comprehension to count length of each word in a sentense (take input from user)

sentence = input("Enter sentence: ")
words = sentence.split()

dict1 = {word : len(word) for word in words}

print(dict1)