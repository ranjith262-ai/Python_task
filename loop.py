"""
for num in range(1,11):
    print(num)

for char in "python":
    print(char)

add = 0
for num in range(1,11):
    add = num+add
    print("Sum of:", add)

department = ["CSE","IT","ECE","EEE","MECH"]
for depar in department:
    print("Department list:", depar)

for num in range(10,20):
    if num % 2 == 0:
        print("Display even numbers:", num)
       
for num in range(20,51):
    multiple = num * 5
    print("Multiple of 5s:", multiple)

new = 1
for num in range(1,6):
    new = new * num
    print("Factorial of 5 is:", new)

new = int(input("Enter the numbers:" ))
for num in range(new):
    if num != 0:
        new = new * num
        print("number is non-zero so product of numbers is:", new)
print("number is zero")

new = int(input("Enter the numbers:" ))
for num in range(new):
    print(f"number to add {num} with {new}")
    if num >= 1:
        new = new + num
        print(f"number is non-negative so sum of numbers is:", new)
    else:
        print(f"user enter the number is negative {num}")
#print(f"user enter the number is invalid {new}")
#print("number is negative")
"""


