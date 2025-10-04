#Longest prefex from set of string
set1 = {"catagory", "cat", "catlog", "cattery"}

list1 = list(set1)
prefix = ""
minword = min(list1)  # smallest word by length

for i in range(len(minword)):
    char = minword[i]
    if all(word[i] == char for word in list1):
        prefix += char
    else:
        break

if prefix:
    print("Longest common prefix:", prefix)
else:
    print("No common prefix")

        