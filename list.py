"""
lst = [10,20,11,16,17,22,47]
for i in lst:
    if i%2==0:
        #lst.append(i)
        print("Even number:", i)
    else:
        print("Odd number:", i)
"""
#exercise:2
lst2 = [10, 20, 30, 40, 50, 1]
lst3 = 0
for i in lst2:
    lst3 = lst3 + i
print("Sum of all elements in the list:", lst3)

#exercise:3
lst4 = [10, 20]
lst5 = 1
for i in lst4:
    if i > 0:
        lst5 = lst5 * i
print("Multiplication of all elements in the list:", lst5)

#exercise:4
lst6 = [10, 20, 20, 40]
lst7 = []
for i in lst6:
    if i not in lst7:
        lst7.append(i)
print("List after removing duplicates:", lst7)

#exercise:6
lst8 = [10, 20, 30, 40, 50]
lst9 = []
for i in range(len(lst8) - 1, -1, -1):
    lst9.append(lst8[i])
print("Reversed list:", lst9)

#exercise:5
lst10 = [10, 20, 30, 40, 50, 11, 7, 3, 90, 100]
small_num = lst10[0]
large_num = lst10[0]
for i in lst10:
    if i < small_num:
        small_num = i
    if i > large_num:
        large_num = i
print("Smallest number in the list:", small_num)
print("Largest number in the list:", large_num)


        

        
    