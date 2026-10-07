
# list is a  mutable and we can add difrent type of datatypes in list


marks = [22,44,54,92,"shahid",3,4,5,4,443,3,23,2]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])


if 40 in marks:
    print("yes")
else:
    print("no")


if "sha" in "shahid":
    print("yes")
else:
    print("no")


# jump indexing
print(marks[0:-1])
print(marks[0:-1:2])

# lisr comprihentions
lst= [i*i for i in range(10)]
print(lst)

lst= [i*i for i in range(10) if i%2==0]
print(lst)
