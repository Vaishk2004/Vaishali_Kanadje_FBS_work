#Program to find the larger string without using build in function
str1 = input("Enter string first: ")
str2 = input("Enter string second: ")

count1 = 0
count2 = 0
for i in str1:
    count1 += 1

for i in str2:
    count2 += 1

if count1 > count2:
    print("First string is large")
elif count1 < count2:
    print("Second string is large")
else: 
    print("Both have same length")