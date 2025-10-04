#Program to sort the list according to length of the elements within the sublist

list1 = [[12,2,45],[2,43,7,89],[23,23,4],[23,4],[23,78]]
print(list1)

for j in range(1,len(list1)):
    for i in range(len(list1)-j):
        if len(list1[i]) > len(list1[i+1]):
            list1[i],list1[i+1] = list1[i+1],list1[i]
        
print("List after sorting: ",list1)