# a= int(input("enter a number:"))
# b= int(input("enter b number:"))

# a=4
# b=44

# # a= input('enter number 1:')
# b= input('enter something  : ')

# # print(a + b)
# # print(a*b)
# # print(a - b)
# # print(a / b)

# # print(str(a)+str(b))
# # print(int(a)+int(b))

# n= len(b)

# for i in b :
#     print(i)


# a= '''bhai tu to apna aadmi hai na
# or bata kaise hgaal hai 
# lekin tu bata '''
# b='eo bol raha tha ke "shahid bahot accha ladka hai"'
# c='eo bol raha tha ke \'shahid bahot accha ladka hai\''
# print(c[:10])
# # print(b)
# # print(c)

# # for character in a:
# #     print(character)

# nm= "harry"
# print(nm[-4:-1])



a= "Shahid !!!!!!!!!!!!!!!! Shahid "

print(len(a))
print(a.upper())
print(a.lower())
print(a.strip("!"))
print(a.replace("Shahid","bidu"))
print(a.split(" "))

heading = "this is a best to the world and work is going "
print(heading.capitalize())

str1 = "welcome to the console"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Shahid"))


str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))
str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4,10))

print(str1.find("to"))
print(str1.find("tofwd"))
# print(str1.index("toscvdc"))

str1 = "Welcome To The Console"
print(str1.isalnum())
print(str1.isalpha())

str = "welcome to the console \n!!!"
print(str.islower())
print(str.isprintable())

b="      "
print(b.isspace())

print(str1.istitle())
print(str.istitle())
print(str.swapcase())
