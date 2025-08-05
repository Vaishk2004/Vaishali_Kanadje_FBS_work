# Print all numbers which are divisible by m ans n in list
list1 = []
num = int(input("Enter number of element in list: "))
for i in range(num):
    list1.append(int(input()))
print(list1)


m = int(input("Enter m number: "))
n = int(input("Enter n number: "))
for i in range(num):
    if list1[i] % n == 0 and list1[i] % m == 0:
        print(list1[i])