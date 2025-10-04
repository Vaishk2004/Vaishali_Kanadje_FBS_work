# Program that find all pairs of element in list whose sum is equal to given value
list1 = [12,4,54,8,5,89,3,2,5,78]

value = int(input("Enter value which is check as sum of two element: "))

for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if value == list1[i] + list1[j]:
            print(list1[i],list1[j])