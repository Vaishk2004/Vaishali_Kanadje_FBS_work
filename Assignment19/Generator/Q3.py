# Generator function that mimics the behavior of the build in function range() function
# The generator should take start ,stop,and step arguments and yield numbers within the specified range

def genRange(start,stop,step):
    for i in range(start,stop,step):
        yield i

start = int(input("Enter start: "))
stop = int(input("Enter stop: "))
step = int(input("Enter step: "))

number = genRange(start,stop,step)
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))