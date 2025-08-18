# D =[2000,500,200,100,50,20,10,5]
# Accept amount from user and calculate the number of notes required

note = [2000,500,200,100,50,20,10,5]

amount = int(input("Enter amount: "))
notes = 0
i = 0
while(amount!= 0):
    a = amount// note[i]
    amount = amount % note[i] 
    notes += a
    i += 1

print("Number of notes: ",notes)