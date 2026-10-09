for i in range(11):
    print("i love you ",i)     # when loop is complete then else exicute
else:
    print("i dont love you back")


for i in range(11):
    print("i love you ",i)
    if i ==6: 
        break
else:            # loop is not completed it is break there for eles will not exicute
    print("i dont love you back")


i = 0
while i<7:
    print(i)
    i= i+1
else:          # when loop is complete then else exicute
    print("sorry no i")


i = 0
while i<7:
    print(i)
    i= i+1
    if i ==5:
        break
else:   # loop is not completed it is break there for eles will not exicute
    print("sorry no i")

