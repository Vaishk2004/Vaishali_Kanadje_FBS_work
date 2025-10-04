# Develop a Memoization decorator that caches the result of function calls and returns the cached result when the same inputs occur again .
# This can greatly improve the performance of recursive or computationally intensive function

def memory(fun1):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        
        else:
            res = fun1(n)
            cache[n] = res
            return res
    return wrapper
        
@memory
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

print(factorial(5))
print(factorial(4))
print(factorial(5))
print(factorial(3))