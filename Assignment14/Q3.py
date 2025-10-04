#Program to find all unique words and count the frequency of occurance from a given list of string

list1 = ['Python', 'Hello', 'Firstbit', 'Hello', 'world','Python']

dict1 = {}
for word in list1:
    if word in dict1:
        dict1[word] += 1
    else:
        dict1[word] = 1

print("Unique words:", set(dict1.keys()))
print("Word frequencies:", dict1)
