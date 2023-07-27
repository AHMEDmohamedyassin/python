print('\n\n\n\n\n' , 'string methods'.center(50 , '#') , '\n\n\n')
#################################################
# string methods
#################################################
text , a = """ multible
line string
""" , 'python is a programming LANGUAGE python is easy'  ## zfill 

print('text string : ' , text)
print('a string : ' , a)

#indexing
print('indexing : ' , a[5])

#slicing [start:end:step]
print('slice : ' , a[12:24:1])
print('slice : ' , a[::3])

#strip() 
b = '    python      '
c = '#@#@#@python#@#@#@'
print('strip : ' , b.strip())
print('lstrip : ' , b.lstrip())
print('rstrip : ' , c.rstrip('#@'))

#title , capitalize , upper , lower
print('title : ' , a.title())
print('capitalize : ' , a.capitalize())
print('upper : ' , a.upper())
print('lower : ' , a.lower())

#split
print('split : ' , a.split(' ' , 3))
print('reverse split : ' , a.rsplit(' ' , 3))

#center(width , fill char) , rjust(width , fill char) , ljust(width , fill char)
print('center : ' , a.center(60 , '#'))   ## عدد الحروف يضاف عليه عدد من الرمز يساوي خمسين
print('rjust : ' , a.rjust(60 , '#'))
print('ljust : ' , a.ljust(60 , '#'))

#count(word , start , end)
print('count (repeate of python word) : ' , a.count('python'))

#swapcase()  convert uppercase to lower case and vice versa
print('swapcase : ' , a.swapcase())

#startswith(sensitive word , start , end) ,  endswith()
print('startswith : ' , a.startswith('p'))
print('endswith : ' , a.endswith('n' , 0 , 6))

#index(substring , start , end)    // if not found gives error and stop code
print('indexs : ' , a.index('t' , 2 , 10))

#find(substring , start , end)    // if not found giver -1
print('find : '  , a.find('y' , 3 , 5)) 

#splitlines()
print('splitlines : ' , text.splitlines())

#expandtabs()
d = 'python\tis\ta\tprogramming\tlanguage'
print('expandtabs : ' , d.expandtabs(10))

#istitle , isspace , islower , isidentifier
print('istitle for string (a): ' , a.istitle())
print('isspace for string (a): ' , a.isspace())
print('islower for string (a): ' , a.islower())
print('isidentifier for string (a) means that this string can be variable name or not: ' , a.isidentifier())

#replace(old value , new value , count)
print('replace (python , php , 2)' , a.replace('python' , 'php' , 2))

#"-".join(list)
e = ['python' , 'php' , 'javascript']
print('join list : ' , ' and '.join(e))


print('\n\n\n\n\n' , 'string formatting'.center(50 , '#') , '\n\n\n')
#####################################################
# string formatting
#####################################################

name = 'ahmed mohamed' 
age = 22
rate = 98.2926829

print('old format type : \n full name is >>>"%s" while first name is >>>"%.5s" and age is >>>"%d" while in hundred term age is >>>"%.3d" and rate is >>>"%f" while simpled rate is >>>"%.2f" \n' % (name , name , age , age , rate , rate))

print('new format type : \n full name is >>>"{0:s}" while first name is >>>"{0:.5s}" and age is >>>"{1}" while in hunderd term age is >>>"{1:3d}" and rate is >>>"{2:f}" while simpled rate is >>>"{2:.2f}" \n '.format(name , age , rate))

print(f'python 3.6+ format type : \n full name is >>>{name} while first name is >>>"{name[0:5]}"')



print('\n\n\n\n\n\n' , 'integer'.center(50 , '#') , '\n\n\n')
####################################################
# integers
####################################################

theinteger = 10
thefloat = 10.6
print('contver int to float : ' , float(theinteger) , '\tcontver float to int : ' , int(thefloat))
print('flooring devision : ' , 110 // 20)
print('Exponent (power) : ' , 5 ** 2)
print('Modulus (باقي القسمة) : ' , 5 % 2 )


print('\n\n\n\n\n\n' , 'lists'.center(50 , '#') , '\n\n\n')
##################################################
# lists
##################################################
thelist = ['php' , 'python' , 'js' , 'c++' , 'c' , 'go']

print('list slicing : ' , thelist[1:6:2])
thelist[1:3] = []
print('edited list : ' , thelist)

#append
thelist.append(['python' , 'c#'])
thelist.append(200)
print('append : ' , thelist)

#extend
thelist.extend([100 , 200 , 300])
print('extend : ' , thelist)

#remove     make error if value isnot found
thelist.remove('go')

#pop
print('pop item : ' , thelist.pop(-1))

#sort 
unsorted = [3 , 7 , 1 , 6 , 2 , 9 , 10]
unsorted.sort(reverse=True) 
print('sorted list : ' , unsorted)

#reverse
thelist.reverse()
print('reversed list (reverse without ordering) : ' , thelist)

#clear()

#copy  // shallow copy
thelistB = thelist.copy()

#count()     // get item repeat
print('count (get item repeat) : ' , thelistB.count(200))

#index()
print('index  : ' , thelistB.index(200))

#insert   ## place new item before detected index
thelistB.insert(2 , "test")
print('insert (add element before detected index) : ' , thelistB)


print('\n\n\n\n\n\n' , ' tuple '.center(50 , '#') , '\n\n\n')
##################################################
# tuple
##################################################
thetuple = (1,2,3,4,5,6,9)