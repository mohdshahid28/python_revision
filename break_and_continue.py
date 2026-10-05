# break function is use for to 
# exit the loop but the continue 
# function use to skip the iteration only and 
# contineu for next value


# using break and continue for (for loop)
# using break

for i in range(15):
    if (i == 10):
        break
    print(" 5 X",i+1, "=", 5*(i+1))

print("exit the loop")

# using continue for loops

for i in range(15):
    if (i == 11):
        print("exit the iteration")
        continue
    if (i == 13):
        print("exit the iteration")
        continue
    print(" 5 X",i, "=", 5*i)

i = 0
while True:
    print(i)
    i = i+1
    if(i%100 == 0):
        break
    