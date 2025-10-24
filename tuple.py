#exercise:1
tuplelist = (1, 2, 3, 4, 5)
tuplelist1 = list(tuplelist)
for item in range(6,11,1):
    tuplelist1.append(item)
    tuplelist = tuple(tuplelist1)
print(tuplelist)

#exercise:2
tupledata = ("python", "C", "C++")
tupledata1 = list(tupledata)
for item1 in ("Java", "JavaScript"):
    tupledata1.append(item1)
    tupledata = tuple(tupledata1)
print(tupledata)