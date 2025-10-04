#Given two sets of numbers,with python program to find missing number in second set as compare to first and vise versa 

set1 = {12,43,5,34,7,75,71}
set2 = {7,34,71,8,46,23,98,4,32}

miss_num1 = set()
miss_num2 = set()

for i in set1:
    if i not in set2:
        miss_num1.add(i)


for i in set2:
    if i not in set1:
        miss_num2.add(i)

print("Missing number in second set as compare to first: ",miss_num1)
print("Missing number in first set as compare to second: ",miss_num2)


