        #          1   
        #       1     1
        #    1     2     1
        # 1     3     3     1


for i in range(1,5):
    for j in range(0,5-i+1):
        print("  ",end=" ")

    x = 1
    for j in range(1,i+1):
        print(" ",x," ",end =" ")
        x = x * (i-j)//j
    print()