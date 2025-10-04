#Implement generator function that yields palindrome numbers.
#Generate palindrome lazily and infinitely

def genPalin():
    for num in range(100,10000):
        temp = num
        rev = 0
        while(num != 0):
            a = num % 10
            num = num // 10
            rev = (rev * 10) + a
        if(temp == rev):
            yield temp

result = genPalin()
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
