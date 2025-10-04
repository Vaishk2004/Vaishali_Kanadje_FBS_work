# we want to generate fibonacci series upto givwn limit.
# Instead of computing and storing the entire sequence in memory 
# Crete generate to yield fibonacci number one by one , conserving memory and allowing for easy iteratiom

def genFibo(n):
    a = -1
    b = 1
    for i in range(n):
        c = a + b
        a = b
        b = c
        yield c


num = int(input("Enter number: "))
result = genFibo(num)

print(next(result))
print(next(result)) 
print(next(result))
print(next(result))
print(next(result)) 
print(next(result))

