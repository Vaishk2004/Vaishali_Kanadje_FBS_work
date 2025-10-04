# Python program for finding intersection of two lists
n = int(input("Enter range of lists: "))
list1 = []
list2 = []
for i in range(n):
    list1.append(int(input()))
print("First list: ",list1)

for i in range(n):
    list2.append(int(input()))
print("Second list: ",list2)

intersection = []

for i in range(n):
    x = list1[i]
    for j in range(n):
        if x == list2[j] and x not in intersection:
            intersection.append(x)

print("Intersection: ",intersection)
