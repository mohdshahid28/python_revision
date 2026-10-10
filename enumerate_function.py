marks = [12,56,32,33,98,1,4,66,67]

index= 0
for mark in marks:
    print(mark)
    if(index == 4):
        print("shahid, awesome")
    index +=1


# enumerate(): Python mein enumerate()
#  kisi list ya sequence ke har item ke 
# saath uska index (number) deta hai.

# example=1
for index, mark in enumerate(marks):
    print(mark)
    if(index == 4):
        print("shahid, awesome")

#example=2     
for index, mark in enumerate(marks, start=1):      #we can decide start index
    print(mark)
    if(index == 4):
        print("shahid, awesome")

#example=3
names = ["Ali", "Rahul", "Aman"]

for index, name in enumerate(names):
    print(index, name)