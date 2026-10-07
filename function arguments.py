# this is a requred argument for function

def avarage(a, b):
    print("the avarage requred argument is ", (a+b)/2)

avarage(4,5)

# this is a default argument

def avarage(a=6, b=9):
    print("the avarage of default arguments is ", (a+b)/2)

avarage()
avarage(8)
avarage(9,2)

def name(fname, mnane="shahid", lname="ansari"):
    print("hello", fname, mnane, lname)

name("arbaz",'shahid','shaikh')
name("mohd","sameer")
name("mohd")

# keyword argument
def avarage(a=6, b=9):
    print("the avarage of default arguments is ", (a+b)/2)
avarage(b=4, a=9)



# arbitrary argument
def navarage(*numbers):
    # single * means tuple 
    sum=0
    for i in numbers:
        sum= sum+i
    print("avarage is: ", sum/len(numbers))


navarage(4,6,9)

# using dictionary in functions
def name(**name):
    print("hello", name["fname"],name["mname"],name["lname"])

name(mname="sd", lname="ansari", fname= "shahid")



def navarage(*numbers):
    # single * means tuple 
    sum=0
    for i in numbers:
        sum= sum+i
    return sum/len(numbers)

a= navarage(4,6,9)
print(a)