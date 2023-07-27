################ func ############################
education = {'school' : 'abo_baker' , 'university' : 'CEV'}
def func(name = '' , *skills , edu , **others) :
    print(f'hello {name} , your skills is : ')
    for skill in skills :
        print(skill)

    for education , value in edu.items() : 
        print(f"title : {education} ===>>> value : {value}")

    for oth , value in others.items():
        print(f"title : {oth}  ===>>>  value : {value}")

# func("ahmed" , "html" , "css" , edu = education , myname = "ahmed mohamed yassin")

################ word function ##############################
word = "wwwoorrrrrddssss"
def word_func(words):
    w = ""
    for word in words:
        if w[-1:] != word :
            w += word
    print(w)

# word_func(word)

#################### anomynous function ####################

hello_function = lambda name = 'unknown' , age = 'unknown' : print(f'hello {name} , your age is {age}')

# hello_function("ahmed" , 21)

################### files handle #################
# modes => r : read , a : append تكتف في الملف بدون حذف المكتوب , w : write تكتب في الملف و تحذف الموجود

import os

# print('current working dir : '  + os.getcwd())
# print('current file path : ' + __file__)
dirname = os.path.dirname(os.path.abspath(__file__))

file = open(fr"{dirname}\text.txt" , "r")    ##### r علشان ميعتبرش ان ال\ مقصودة سطر جديد مثلا

print(f"""
file name : {file.name} , 
file mode : {file.mode} , 
file encoding : { file.encoding} , 
""")

# print(file.read())       ## يقرا المحتوي كله
# print(file.readline(1))
# print(file.readline())   ## يقرأ سطر و أكثر من واحدة يقرا الصف التالي
# print(file.readlines())  ## يقوم بإرجاع الأسطر في مصفوفة
# print(file.readlines(10)) ## يقوم بإرجاع الأسطر قي مصفوفة لكن يتم تحديد الحد الأقصي لمساحة الليانات

file.close()

file = open(fr"{dirname}\text2.txt" , "w")
file.write("hello from python")

file = open(fr"{dirname}\text2.txt" , "a")
file.write('hello from python')

file.truncate(14)    ## حذف ما هو دون عدد اللي متحدد
print(file.tell()) ## مكان وقوف المؤشر

file = open(fr"{dirname}\text2.txt" , "r")
file.seek(4)     ##  يحدد مكان المؤشر
print(file.read())

file.close()

# os.rename(fr"{dirname}\text2.txt" , 'pytonTestFile.txt')

os.remove(fr"{dirname}\text2.txt")     ## حذف الملف
