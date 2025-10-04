# python program to find all  the anagrams and group them together from a given list of strings

lists = ['silent','hello','listen','god','dog','spell','hello','eollh']

anagram  = {}

for word in lists:

    key = ''.join(sorted(word))
    
    if key in anagram:
        anagram[key].append(word)
    else:
        anagram[key] = [word]

# Print groups
for group in anagram.values():
    if len(group) > 1:  
        print(group)
