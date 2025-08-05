#Program to find maximum and minimun element in list
list1 = []
num = int(input("Enter how many element you want in list: "))
for i in range(num):
    ele = int(input())
    list1.append(ele)
print(list1)

max = list1[0]
for i in range(num):
    if max < list1[i]:
        max = list1[i]
    
print("Maximum element: ",max)

min = list1[0]
for i in range(num):
    if min > list1[i]:
        min = list1[i]
    
print("Minimun element: ",min)
