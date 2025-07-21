#           1 
#         2 3 2
#       3 4 5 4 3
#     4 5 6 7 6 5 4
#   5 6 7 8 9 8 7 6 5


for i in range(1,6):
    for j in range(1,7-i):
        print(" ",end=" ")
    x = i
    for j in range(1,i+1):
        print(x,end=" ")
        x+=1
    k=j-2
    for j in range(1,i):
        print(k+i,end=" ")
        k-=1
    print()

    