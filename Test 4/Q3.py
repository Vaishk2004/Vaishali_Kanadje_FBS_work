#Print pattern

for i in range(1,11):
    for j in range(10,1,-1):
        if i==1 or i==10 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()