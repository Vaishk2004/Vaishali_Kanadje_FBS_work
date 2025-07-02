#Reverse the three digit number
num = int(input("Enter the three digit number:"))#consider 345

a = num % 10 #5
num = num // 10 #34
b = num % 10 #4
revers = (a*10)+b #54
c = num // 10 #3
revers = (revers * 10) + c

# revers = a*100 + b*10 +c
print("Reverse Number is:",revers)
