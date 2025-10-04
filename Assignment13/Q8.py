#Program to count frequency of words apeearing in a string using a dictionary
str1 = "Hello Firstbit Solutions Hello hello"

dict1 = {}

for word in str1.split():
    if word in dict1:
        dict1[word]+=1
    else:
        dict1[word]=1

print("Frequency of words in string: ")
for x,y in dict1.items():
    print(x,"=",y)