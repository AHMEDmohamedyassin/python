# built in functions
# any()
# all() 
# bin()
# id()
# sum()
# round()
# range()  start , end , step
# print() 
# pow()
# min()
# max()
# enumerate(list here , counter start from optional number )
# reversed(list or string )
# map(function , list or tupule)
# filter(function , list or tupule)
# reducer(function , list or tupule)
a = [1 , 2 , 3 , 4]
if any(a) : 
    print('علي الأقل يوجد عنصر ليس ب false')
else : print('لا يوجد عنصر قيمته true')

if all(a) : 
    print('كل العناصر ب true')

print(bin(200))

print(sum(a , 20))    # قام بجمع المصفوفة و زاد عليها ب 20
print(round(23.658 , 2))   # الرقم الثاني هو عدد الأرقام العشرية
print(list(range(20 )))
print(list(range(6 , 20 , 2)))
print('ahmed' , 'mohamed' , "yassin" , sep=" / "  , end="\t the next line :   ")
print('ahmed' , 'mohamed' , "yassin" , sep=" @ " )

mappedData = map(lambda num : num + 2 , a)
filteredData = filter(lambda num : num > 2 , a)

for mp in mappedData :
    print(mp)
print("#" * 20)
for mp in filteredData :
    print(mp)

from functools import reduce

reducedData = reduce(lambda num1 , num2 : num1 + num2 , a)
print('#' * 20 , reducedData , sep="\n")

