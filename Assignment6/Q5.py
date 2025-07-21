#                  *  

#              *   *   *

#          *   *   *   *   *

#      *   *   *   *   *   *   *

#  *   *   *   *   *   *   *   *   *
for i in range(1,10):
    for j in range(1,10-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        if(i % 2 != 0):
            print(" * ",end=" ")
        
    print()
    