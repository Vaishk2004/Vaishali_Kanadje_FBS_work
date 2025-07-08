# Calculate the total amount will be pay 
a1 = int(input("Enter the age of First Person: "))
a2 = int(input("Enter the age of Second Person: "))
a3 = int(input("Enter the age of third person: "))
a4 = int(input("Enter the age of four person: "))
a5 = int(input("Enter the age of fifth person: "))
amount = int(input("Enter Ticket Amount:"))
total = 0

if(a1 < 12):
    total += amount - (amount * 0.3) # 30% Discount for child
elif(a1 > 59):
    total += amount - (amount * 0.5) # 50% Discount senior
else:
    total += amount #No Discount adult

if(a2 < 12):
    total += amount - (amount * 0.3) #amount * 0.7
elif(a2 > 59):
    total += amount - (amount * 0.5) #amount * 0.5
else:
    total += amount

if(a3 < 12):
    total += amount - (amount * 0.3)
elif(a3 > 59):
    total += amount - (amount * 0.5)
else:
    total += amount

if(a4 < 12):
    total += amount - (amount * 0.3)
elif(a4 > 59):
    total += amount - (amount * 0.5)
else:
    total += amount

if(a5 < 12):
    total += amount - (amount * 0.3)
elif(a5 > 59):
    total += amount - (amount * 0.5)
else:
    total += amount

print("Total amount to ticket of travel is : Rs",total)

    
