#Exercise:1

thisset = {1,2,3,4,5,6,7,8,9,10}
thisset1 = list(thisset)
for item in range(11,13,1):
    thisset1.append(item)
    thisset = set(thisset1)
print(thisset)

#Exercise:2

set1 = {"apple", "banana", "cherry"}
set2 = {"orange", "kiwi", "melon", "banana"}
set3 = set1.union(set2)
print(set3)
set4 = set1.intersection(set2)
print(set4)
set5 = set3.union(set4)
set6 = set3.intersection(set4)
print(set5)
print(set6)

#Exercise:3