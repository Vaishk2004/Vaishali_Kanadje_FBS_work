#Program to create a new list from exicting list which contain cube of each number of list
list1 = []
n = int(input("How many number you want in list: "))
for i in range(n):
    list1.append(int(input()))


cube = []
for i in range(len(list1)):
    ans = list1[i] ** 3
    cube.append(ans)

print("Existing list: ",list1)
print("New List: ",cube)