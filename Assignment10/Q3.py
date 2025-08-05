#Second largest element in the list
list1 = []
n = int(input("How many number you want in list: "))
for i in range(n):
    list1.append(int(input()))
print(list1)


large = list1[0]
sec_large = 0
for i in range(1,len(list1)):
    if large < list1[i]:
        sec_large = large
        large = list1[i]
    elif sec_large < list1[i]:
        sec_large = list1[i]

print("Second Large: ",sec_large)