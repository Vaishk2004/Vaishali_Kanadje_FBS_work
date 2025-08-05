# Accept number from user and find it is in list or not 
#Also tell how many time is present in list

list1 = []
n = int(input("How many number you want in list: "))
for i in range(n):
    list1.append(int(input()))
print(list1)


num = int(input("Enter number: "))
for i in range(len(list1)):
    if num in list1:
        print("Present")
        break
else: 
    print("Not present")


count = 0
for i in range(len(list1)):
    if num == list1[i]:
        count+=1
    
print("Number of occurance: ",count)