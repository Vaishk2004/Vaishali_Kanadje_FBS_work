#Write a function which pass the parameter and print factors of a given number

def factor(num):
    for i in range(1,num+1):
        if num % i == 0:
            print(i,end=" ")
    
num = int(input("Enter number: "))
print(f"Factors of {num} : ")
factor(num)