# Write a program to form new string where the first character and last character have been exchange
str = input("Enter string: ")

if len(str)<2:
    new_str = str
else:
    new_str = str[-1]+str[1:-1]+str[0] #Slicing will be used last char + middle + first char

print("New string: ",new_str)
    
