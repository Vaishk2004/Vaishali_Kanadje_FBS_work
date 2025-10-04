#Python program to sort the list According to the second element in the sublist

list1 = [[1,2,34],[2,4,12],[12,5,34],[223,1,23]]

print(list1)

for j in range(1,len(list1)):
    for i in range(len(list1)-j):
        if list1[i][1] > list1[i+1][1]:
            list1[i],list1[i+1]= list1[i+1],list1[i]
print("After sorting accourding to the second element in sublist: ",list1)
