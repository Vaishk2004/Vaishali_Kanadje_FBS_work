for i in range(1,6):
    for j in range(1,6):
        if(i%2!=0):
            if(i%2==0 or j%2==0 ):
                print("0",end=" ")
            else:
                print("1",end=" ")
        else:
            if(i%2!=0 or j%2!=0 ):
                print("0",end=" ")
            else:
                print("1",end=" ")
    print()