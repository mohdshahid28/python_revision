

questions = [
    ["Which language is used to create VS Code?", "Python", "French", "JavaScript", "PHP", 3],
    ["Who developed Python?", "Dennis Ritchie", "Guido van Rossum", "James Gosling", "Bjarne Stroustrup", 2],
    ["What does CPU stand for?", "Central Processing Unit", "Computer Personal Unit", "Central Program Utility", "Control Processing Unit", 1],
    ["Which language is used for web page styling?", "Python", "Java", "CSS", "C++", 3],
    ["Which company developed Windows?", "Apple", "Google", "Microsoft", "IBM", 3],
    ["What does HTML stand for?", "Hyper Text Markup Language", "High Text Machine Language", "Hyper Transfer Markup Language", "Home Tool Markup Language", 1],
    ["Which data type stores True or False?", "String", "Boolean", "List", "Integer", 2],
    ["Which symbol is used for comments in Python?", "//", "<!-- -->", "#", "/* */", 3],
    ["Which keyword defines a function in Python?", "function", "define", "fun", "def", 4],
    ["Which data structure stores key-value pairs in Python?", "Tuple", "Set", "Dictionary", "String", 3],
    ["Which company developed Java?", "Sun Microsystems", "Microsoft", "Meta", "Intel", 1],
    ["What is the output of 2 ** 3 in Python?", "6", "8", "9", "5", 2],
    ["Which method adds an item to a Python list?", "add()", "insertEnd()", "append()", "push()", 3],
    ["Which keyword is used to handle exceptions in Python?", "catch", "error", "final", "except", 4]
]

levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1280000,3000000, 10000000]

money= 0

for i in range(0, len(questions)):
    question= questions[i]
    print(f"your nextquetion is \n {question[0]}")
    print(f"Question for Rs.{levels[i]}")
    print(f"a. {question[1]}            b. {question[2]}")
    print(f"c. {question[3]}            d. {question[4]}")
    reply = int(input("enter your answer (1-4): "))
    if(reply== question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if(i==4):
            money= 10000
        elif(i== 9):
            money= 320000
        elif(i== 14):
            money= 10000000
    else:
        print("Wrong answer!")
        break
print(f"Your take home money is {money}")