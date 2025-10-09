"""
char1 = "Hello, World"
char2 = '  Python Programming'
print(char1[0])
print(char1[1:5])
print(char1[2:])
print(char1[:2])
print(char1[-5:-2])
print(char1.upper())
print(char1.lower())
print(char2.strip())
print(char2.replace("  ", "Hello "))
print(char1.split(","))
print("Hello" in char1)
if "Hello" in char1:
    print("Yes string is present")
else:
    print("No string is not present")
if "hello" not in char1:
    print("Yes string is not present")
else:
    print("No string is present")

a = "hello"
b = "world"
c = a + " " + b
print(c)

age = 25
txt = f"My name is John, and I am {age}"
print(txt)
"""
#exercise:1
char4 = """Python is a popular, high-level, general-purpose programming language known for its simple syntax, readability, and extensive libraries, used for web development is, data science, automation, machine learning, and more"""
print(char4)
print(char4.replace("is", "was"))
print(char4.count("a"))

#exercise:2
char5 = input("Enter your email id: ")
if "@" in char5:
    print("Yes its email id")
else:
    print("No its not email id")

if char5.endswith(".com"):
    print("Yes its website link")

#exercise:3
char6 = input("enter your password: ")
if len(char6) < 8:
    print("Password must be at least 8 characters long")
else:
    print("Strong password")

#exercise:4
password = input("Enter your password: ")
if "@" in char5 and password == char6:
    print("Login successful")
