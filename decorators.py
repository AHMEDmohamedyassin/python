################### decorator ################

def myDecorator (func):
    def decorator (na):
        print('before')
        func(na)
        print('after')
    return decorator

def myDecorator2(func) : 
    def dec(na):
        print('decorator 2')
        func(na)
    return dec

# طريقة غير مستخدمة بكثرة
# def sayHello(): print('say hello')
# decoratedSayHello = myDecorator(sayHello)
# decoratedSayHello()

@myDecorator
@myDecorator2
def sayHello(name): print(f'say hello {name}')

# sayHello("ahmed")


############### zip #################
list1 = [1,2,3,4,5,6,7,8,9,10]
tuple1 = (1,2,3,4,5,6)
dic1 = {"name" : "ahmed" , "phone" : "01066404523" , "country" : "Egypt"}

# for item1 , item2 , item3 in zip(list1 , tuple1 , dic1) :
    # print(f"list 1 => {item1} \n tuple1 => {item2} \n dic1 => key: {item3} , value : {dic1[item3]}")

### 87 , 89

################### Exception handle errors ########################
num = 10

# if type(num) == int :
    # raise ValueError('number is integer')
    # raise Exception('number is integer')

# try :
#     number = int(input('enter your age : '))
# except : 
#     print('value is not integer')
# else : # fired if no error ممكن احط محتواها في ال try
#     print('no error')
# finally :
#     print('finally printed at any condition if there is error or not')


# file open example 

# file_tries = 5

# while file_tries > 0 :
#     try :
#         print(f"enter absolute path of file to open , you have {file_tries} remains ")
#         file_path = input('enter file path : ')
#         file_tries -= 1
#         the_file = open(file_path  , "r")
#         print(the_file.read())
#         the_file.close()
        
#         break
#     except FileNotFoundError :
#         print('file not found')
#     except : 
#         print('something went wrong') 
# else :
#     print('tries ended')     

############## regular excepresion ##############
import re

# print("( AH 123 a) => \s[A-Z]{2}\s[0-9]{3}\s\w{,6}") 
# print('ahmedmohamed@gmail.com => [A-z0-9\.]+@[A-z0-9]+\.[A-z]+')

mysearch = re.search("[a-z]+" , "AhmedMohamed").group()    # search تبحث فقط عن أول عنصر موافق
mysearch = re.findall("[a-z]+" , "AhmedMohamed")    # search تبحث كل العناصر الموافقة
print(mysearch)

print("#" * 50)

mysearch = re.split('\s' , 'Ahmed mohamed yassin')
print(mysearch)

for count , val in enumerate(mysearch):
    print(f"number is {count}    =>   {val}")

print("#" * 30)

print( re.sub('\s|/|_' , '---' , 'Ahmed_mohamed yassin/younes') )

print(re.search(r'(https?)://(www.)?\w+\.\w+(:\d{2,4})?/?(.+)?' , 'https://www.alofoqe.com:8080/mainpage/a/b?search=ahmed').group())