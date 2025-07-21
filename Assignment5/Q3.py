# Accept number of passengers from user and ticket cost.
#Accept age of passenger and calculate the total amount to ticket to travel all of them based on following condition
#a.children below 12 = 30% discount
#b.Senior citizen(above 59)= 50% discount
#c. other need to pay full

num = int(input("Enter number of passenger: "))
cost = int(input("Enter the cost: "))

amount = 0
for i in range(1,num+1):
    age = int(input("Enter age: "))
    if(age<12):
        amount += cost - (cost * 0.30)
    elif(age>59):
        amount += cost - (cost * 0.50)
    else:
        amount += cost
        
print("Total amount to be paid is: ",amount)
        

