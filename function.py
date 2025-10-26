"""
def samplefun(a):
    a = a + 10
    print("This is a sample function:" ,a)
samplefun(5)
samplefun(15)
samplefun(25)
samplefun(35)
samplefun(45)
samplefun(55)

def sumfun(a, b):
    return a + b

print("The sum is:", sumfun(20,100))
"""
#Exercise:1
def square(side):
    area = side * side
    return area
print("The area of square is:", square(5))

#Exercise:2
def rectangle(length, breadth):
    area = length * breadth
    return area
print("The area of rectangle is:", rectangle(5,10))

#Exercise:3
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print("The number is:", even_odd(10))
print("The number is:", even_odd(121))

#Exercise:4
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("The factorial is:", factorial(5))
print("The factorial is:", factorial(7))