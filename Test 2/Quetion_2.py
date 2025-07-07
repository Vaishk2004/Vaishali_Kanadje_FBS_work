num = int(input("Enter the Three digit number: "))

dig3 = num % 10
num = num // 10
dig2 = num % 10
dig1 = num// 10

if(dig1 == 2*dig2 and dig1 == 0.5*dig3):
    print("Yes, you have done it.")
else:
    print("Please try next time.")

