#when we directly import any module we 
# can use its functions my using
#  module name . there function 
# juct like (math.sqrt(9))this
import math
result= math.sqrt(9) * math.pi
print(result)


# we can use this method to import perticular 
# fuction from that module and use (sqrt(9) * pi)
from math import sqrt, pi
result= sqrt(9) * pi
print(result)



#in this import mwthod we can 
# import that all fuctions from 
# module by usingh (*) and now we
#  can use function directly
from math import *
result= sqrt(9) * pi
print(result)

 # we can use module short form 
 # just using as and we can use as 
 # also for fuction name also
import math as m
result= m.sqrt(9) * m.pi
print(result)


#by using (dir) function we can 
# see all the functions in module
import math
print(dir(math))