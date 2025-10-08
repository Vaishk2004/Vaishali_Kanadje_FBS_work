def binarySearch(list1,x):
    start = 0
    end = len(list1)
    while(start <= end):
        mid = (start+end)//2
        if list1[mid] == x:
            return mid
        elif list1[mid]>x:
            end = mid-1
        else:
            start = mid+1
    return -1
 

list1 = []
num = int(input("Enter how many number you want in list: "))

for i in range(num):
    a = int(input("Enter number: "))
    list1.append(a)

print(list1)

list1 = sorted(list1)
print("Sorted list: ",list1)
x = int(input("ENter number for Search: "))

ans = binarySearch(list1,x)
if ans == -1:
    print("Not found")
else:
    print("Found at index: ",ans)

