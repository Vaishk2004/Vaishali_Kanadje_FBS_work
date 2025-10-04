# Print 1 to 100 in snake and ladders pattern
main = []
list1 = []
row = 1
for i in range(1,101):
    list1.append(i)
    if(i%10 == 0):
        if row % 2 == 0:
            list1.reverse()
        main.append(list1)
        row +=1
        list1=[]
    
main.reverse()
print(main)




