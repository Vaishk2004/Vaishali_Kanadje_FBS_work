#Check enter 3 digit number is palindrome or not
num = int(input("Enter 3 digit Number: "))
copy = num

dig1 = num % 10
num = num // 10
dig2 = num % 10
revers = (dig1 * 10) + dig2
dig3 = num // 10
revers =(revers * 10) + dig3


if( revers == copy):
    print("Number is Palindrome.")

else:
    print("Not Palindrome.")

