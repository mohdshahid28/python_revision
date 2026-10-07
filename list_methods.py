# append method
l= [2,3,4,52,3,45,4,8,3,4,4,343,4,55,454]
print(l)

l.append(99)
print("using append",l)


l= [2,3,4,52,3,45,4,8,3,4,4,343,4,55,454]
print(l)

l.sort()
print("using sort",l)
l.sort(reverse=True)
print("using reverse sort",l)
print("using index method",l.index(52))
print("using count method",l.count(4))


# m name ki new list nhi banegi l me hi sab chenge hoga is liye ham copy method use karte hai jisse new list banti hai
# m= l
# m[0]= 0
# print(l)

# using copy method
m= l.copy()
m[0]= 0
print(l)
print(m)


# insert method

l.insert(1,899)
print(l)

# using extend method
m= [900,8000,3400]
l.extend(m)
print(l)

# concatinate merging 2 or more list

n= [90,99900,655480]
k= l+ n
print("k is ",k)