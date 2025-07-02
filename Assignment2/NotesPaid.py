#program to find minimum no. of notes for given amount
amount = int(input("Enter the amount:"))

#500
n500 = amount // 500
r_amount = amount % 500

#200
n200 = r_amount // 200
r_amount %= 200

#100
n100 = r_amount // 100
r_amount %= 100

#50
n50 = r_amount // 50
r_amount %= 50

#20
n20 = r_amount // 20
r_amount %= 20

#10
n10 = r_amount // 10
r_amount  %= 10

print("The Notes to be paid for the amount:",amount)
print("Notes for 500:",n500)
print("Notes for 200:",n200)
print("Notes for 100:",n100)
print("Notes for 50:",n50)
print("Notes for 20:",n20)
print("Notes for 10:",n10)
