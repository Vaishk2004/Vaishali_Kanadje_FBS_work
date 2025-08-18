list1 = [1,3,4,1,2,3,6,7,1,2,4]

dict1 = {}
for num in list1:
    if num in dict1:
        dict1[num] +=1
    else:
        dict1[num] = 1

print(dict1)