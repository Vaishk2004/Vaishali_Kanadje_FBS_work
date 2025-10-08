snake_head = [10,15,50,25,77,33,99]
num = [[100,99,98,97,96,95,94,93,92,91],[x for x in range(90,81)],[x for x in range(81,71,-1)],
       [x for x in range(71,61)],[x for x in range(61,51,-1)],[x for x in range(41,51)],
       [x for x in range(31,41,-1)],[x for x in range(21,31)],[x for x in range(11,21,-1)],
       [x for x in range(1,11)]]

for j in num:
    for i in j:
        if i in snake_head:
            print('>:',end=" ")
        else:
            print(i,end=" ")

    print()

