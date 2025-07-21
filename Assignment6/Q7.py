#                           A   

#                     A     B     C   

#               A     B     C     D     E   

#         A     B     C     D     E     F     G   
   
#   A     B     C     D     E     F     G     H     I   




for i in range(1,10):
    for j in range(1,10-i):
        print("  ",end=" ")
    for j in range(1,i+1):
        if(i % 2 != 0):
            print(" ",chr(64+j)," ",end=" ")
        
    print()