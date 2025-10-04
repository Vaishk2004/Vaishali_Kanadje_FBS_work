#Program to remove the intersection of second set with a first set
set1 = {23,43,78,98,'hybrid',54}
set2 = {35,43,98,9,'Hello','hybrid'}


# intersect = set2.intersection(set1)
# for i in intersect:
#     set1.remove(i)
# print(set1)


# set1.difference_update(set2)  # Removes intersection elements from set1
# print(set1)


for i in set2:
    if i in set1:
        set1.remove(i)
print(set1)