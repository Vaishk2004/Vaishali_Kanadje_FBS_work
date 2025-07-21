# 1 2 3 4 5 
# 2     5 
# 3   5 
# 4 5 
# 5 
for i in range(1,6):
    x = i
    for j in range(1,7-i):
        if(i==1 or j==1 or j==6-i):
            print(x,end=" ")
        else:
            print(" ",end=" ")
        x+=1

    print()

