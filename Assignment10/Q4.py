#Program to reverse the list
list1 = []
n = int(input("How many number you want in list: "))
for i in range(n):
    list1.append(int(input()))
print("Before:",list1)

print("After reverse: ")
print(list1[::-1])

