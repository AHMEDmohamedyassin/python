############################ modules ##########################
import random
from random import randint 
import sys
import ahmedmodule

# print(dir(random))
# print(randint(1 , 100))
# print(random.randint(1 , 100))

# print(sys.path) # يظهر المسارات التي يبحث فيها عن مكتبات

# ahmedmodule.sayHello('ahmed')

############################### date ###########################
import datetime

# print(dir(datetime.datetime.now()))
# print(datetime.datetime.now().time().minute)

birthdate = datetime.datetime(1992 , 4 , 3)
nowdate = datetime.datetime.now()

# print(f"number of days lived is : {(nowdate - birthdate).days} days")

# print(nowdate.strftime("%A / %B / %Y"))    # https://strftime.org


######################### iterator #####################################
mystring = 'ahmed'
iterator = iter(mystring)
# print(next(iterator) , next(iterator) , next(iterator) , next(iterator) , next(iterator) , sep=",") 

def myGenerator():
    yield 1 
    yield 2 
    yield 3

generator = myGenerator()
# print(next(generator) , next(generator) , next(generator)) 