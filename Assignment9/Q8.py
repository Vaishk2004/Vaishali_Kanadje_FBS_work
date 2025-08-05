#Write a function to check whether a function is prime or not

def primeNum(num, i=2):
    if num <= 1:
        return "Not prime"
    if i == num:
        return "Prime number"
    if num % i == 0:
        return "Not prime"
    return primeNum(num, i + 1)

num = int(input("Enter number: "))
print(primeNum(num))
