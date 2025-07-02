#Swapping of two number without using third variable
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
print("The number before swap: ")
print("First number:",num1)
print("Second number:",num2)

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("The number after swap :")
print("First number:",num1)
print("Second number:",num2)

