#Python program foe find second largest element in list using bubble sort
list1 = []
n = int(input("Range for list: "))
for i in range(n):
    list1.append(int(input()))
print(list1)

for j in range(1,len(list1)):
    for i in range(len(list1)-j):
        if list1[i] > list1[i+1]:
            list1[i],list1[i+1] = list1[i+1],list1[i]

print("Second Largest element: ",list1[-2])