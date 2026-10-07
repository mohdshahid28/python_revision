# we can not chenge tuple directly so we use this 
# method and make new tuple with chenges


countries = ("spain", "italy","india","england","germany")
print("old tuple",countries)
temp = list(countries)   #convert to list
temp.append("russia")    #add  item
temp.pop(3)              # remove item
temp[2] = "finland"      #change item
countries= tuple(temp)   #convert to tuple
print("new tuple",countries)


# we can add 2 tuples 
marks1= (22,33,124,145)
marks2= (65,54,63,77,4,4,4,4)
total= marks1+marks2
print(total)



print("using index method",total.index(4)) # search 4 in touple
print("using index method",total.index(4,4,10)) #search number 4 from index 4 to index 10 only
print("using count method",total.count(4))
