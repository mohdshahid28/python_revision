# a= int(input("enter your age: "))
a=119

if (a>18 ):
    print("you can drive")
    if(a>101):
        print("But please try to do not drive this is not good for your health")
elif (a==18):
    print("go and make your licence then you can drive")

else:
    print("you can not drive you have to wait ",18-a ,"years to drive")




import time 
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

if (int(time.strftime('%H'))<12):
    print('Good morning')
if (int(time.strftime('%H'))>12):
    print('good afternoon')