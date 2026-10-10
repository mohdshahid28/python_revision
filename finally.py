   
def func1():    
    try:
        l=[1,3,5,7]
        i = int(input("enter a index: "))
        print(l[i])
        return 1
    except:
        print("some error occurred")
        return 0

    
    print("i will always executed")

x= func1()
print(x)

  #in a fuctions print will not run 
  # after return but if you use finally
  # it will always execute
# 1st is problem and 2nd is solution
def func1():    
    try:
        l=[1,3,5,7]
        i = int(input("enter a index: "))
        print(l[i])
        return 1
    except:
        print("some error occurred")
        return 0

    finally:
        print("i will always executed")

x= func1()
print(x)




