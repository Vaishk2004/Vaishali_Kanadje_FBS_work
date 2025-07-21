#                           1   

#                     1     2     3

#               1     2     3     4     5

#         1     2     3     4     5     6     7

#   1     2     3     4     5     6     7     8     9


for i in range(1,10):
    for j in range(1,10-i):
        print("  ",end=" ")
    for j in range(1,i+1):
        if(i % 2 != 0):
            print(" ",j," ",end=" ")
        
    print()