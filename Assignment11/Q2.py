#Python program to merge two lists and sort it
list1 = []
list2 = []
n = int(input("Enter how many number you want in list: "))

for i in range(n):
    list1.append(int(input()))
print("First list: ",list1)

for i in range(n):
    list2.append(int(input()))
print("Second list:",list2)

list3 = [] 

for i in range(n):
   list3.append(list1[i])
for i in range(n):
   list3.append(list2[i])
   

for i in range(1,len(list3)):
    for j in range(len(list3)-i):
        if list3[j] > list3[j+1]:
            list3[j],list3[j+1]=list3[j+1],list3[j]

print("After merge sorted list: " ,list3)
        