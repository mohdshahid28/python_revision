a= input("enter a number : ")
print(f"Multiplication table of {a} is: ")

for i in range(1,11):
    print(f"{int(a)} X {i} = {int(a)*i}")

# if wrong input it shows error and 
# program end but we neet to continue the 
# program so we use try,except as we use below
print("some important code")
print("end of the program")


a= input("enter a number : ")
print(f"Multiplication table of {a} is: ")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("invalid input")

print("some important code")
print("end of the program")




try:
    num= int(input("enter a number: "))
    a= [6,3]
    print(a[num])
except ValueError:
    print("number enterd is not an integer.")

except IndexError:
    print("Index Error")