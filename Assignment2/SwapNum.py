#Swapping of two number using third variable
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
print("The number Before swap: ")
print("First number:",num1)
print("Second number:",num2)

temp = num1
num1 = num2
num2 = temp

print("The number After swap: ")
print("First number:",num1)
print("Second number:",num2)