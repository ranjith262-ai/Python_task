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

#Exercise:5
def prime_check(chk,num):
    if num <= 1:
        return "Not Prime"
    elif num % chk == 0:
        return "Not Prime"
    return "Prime"
print("The number is:", prime_check(2,346))

#Exercise:6
def reverse_string(char1):
    rev = ""
    for i in range(len(char1)-1, -1, -1):
        rev = rev + char1[i]
    return rev
print("The reversed string is:", reverse_string("Hello world"))

#Exercise:7
def count_char(string):
    count = 0
    for char in string:
        count += 1
    return count
print("The number of characters is:", count_char("Hello"))

#Exercise:8
def sum_square(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total
print("The sum of squares is:", sum_square(5))

#Exercise:9
def polindrome_check(string):
    rev = ""
    for i in range(len(string)-1, -1, -1):
        rev = rev + string[i]
    if string == rev:
        return "Palindrome"
    else:
        return "Not Palindrome"
print("The string is:", polindrome_check("madam"))
print("The string is:", polindrome_check("hello"))

#Exercise:10
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for i in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
print("Fibonacci sequence up to 10 terms:", fibonacci(10))