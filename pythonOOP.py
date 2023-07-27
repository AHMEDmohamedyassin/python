class Food:
    def __init__(self , title):
        self.title = title
        print(f"food title is {self.title}")

    def foodTitle(self):
        return f"the title is : {self.title}"

    def mustImplemented (self):
        raise NotImplementedError('method must be implemented')

class Member(Food) :
    users_number = 0

    def __init__(self , fname , lname , title):
        super().__init__(title)
        self.fname = fname
        self.lname = lname
        Member.users_number += 1

    def __str__(self): # حتي تظهر رسالة مقرؤة توضح وظيفة الكلاس
        return f"this is member class"
    
    def __len__(self):
        return 4
    
    def full_name (self , param) :    # instance method
        return f'hello {self.fname} {self.lname} , param : {param}'
    
    @classmethod
    def counter(cls , param):
        return f'users Number : {cls.users_number} {param}'

    @staticmethod
    def stm (param):
        return f'static method users number : {Member.users_number} , param : {param}'

    def mustImplemented(self):
        return 'implemented method'

user_1 = Member('ahmed' , 'mohamed' , 'tomato')

print(Member.users_number)          # properties (attribute)
print(user_1.full_name("test"))     # instance method
print(Member.counter("test"))       # class method
print(Member.stm('test'))           # static method
print(user_1.__class__)             # getclass name
print(user_1)                       # getclass __str__ message
print(len(user_1))                  # to get len magic method
print(user_1.foodTitle())           # inherited method
print(user_1.mustImplemented())           # inherited implemented method