class Person :
    def __init__(self , name , age):
        self.name = name
        self.age = age
    
    def __str__ (self):
        return self.name
    
    def printing (self) :
        print(f'the name : {self.name}')


class Student(Person):
    def __init__(self , name , age , lname):
        super().__init__(name , age)
        self.lname = lname


a = (1,2,3,4)
b = iter(a)

print(next(b))
print(next(b))
print(next(b))

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = {'name' : 'ahmed' }
print(json.loads(x)['name'] , json.dumps(y))