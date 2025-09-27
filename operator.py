"""
num1 = int(input())
num2 = int(input())
#num3 = 0
if num1 > num2:
    num3 = num1 + num2
    print("addition of num3:" , num3)
elif num1 < num2:
    num3 = num1 - num2
    print("subsraction of num3:" , num3)
else:
    num3 = num1 * num2
    print("multiplication of num3:" , num3)

char1 = str(input())
char2 = str(input())
char3 = char1
#print(char1 is char2)
#print(char1 == char2)
print(char1 is not char2)
"""

char1 = input("Enter the string1:")
char2 = input("Enter the string2:")
#print(char2 in char1)
print(char2 not in char1)
