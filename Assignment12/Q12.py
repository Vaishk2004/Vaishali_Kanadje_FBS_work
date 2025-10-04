#Program to calculate number of lowercase character in strong
str = input("Enter string: ")

count = 0
for i in str:
    if i.islower():
        count += 1

print("Number of lowercase characters:", count)