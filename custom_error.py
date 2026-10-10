a= input("enter a number between 3 to 9: ")
# we can show error using raise keyword

if(a== "quit"):
    print("skip the program")
else:
    a= int(a)

    if a<3 or a>9 :
        raise ValueError("value should be between 3 to 9")
    else:
        print("well done")