import numpy as np
import time 

print(np.__version__)

array1d = np.array([1 , 'a' , True])  # all elements is string
array2d = np.array([[1  , 2] , [1 , 2] , [1 , 2]])    # all elements is number
array3d = np.array([[[1 , 2] , [1 , 2]] , [[1 , 2] , [1 , 2]]]) # all elements is number
custom_array = np.array([1,2,3] , ndmin=3)

print(array1d[0] , array2d[1 , 1] , array3d[1][1][0] , f'dimension number : {array3d.ndim}'  , end=' , ')

print(custom_array)

print(f'slicinc : {array3d[:1 , :1 , :1] }')     #slicing(start:end:step)
############### comparing performance of listing and array
count = 10
mylist1 = range(count)
mylist2 = range(count)
myarray1 = np.arange(count)
myarray2 = np.arange(count)

start_time = time.time()
sum1 = [(n1 + n2) for n1 , n2 in zip(mylist1 , mylist2) ]

start_time2 = time.time()
sum2 = myarray1 + myarray2

print(f'list time : {start_time2 - start_time} ')
print(f'array time : {time.time() - start_time2} ')


print(myarray1.size , myarray1.itemsize)   # .size getting count of elements in array , .itemsize get how many bytes of each item



################### slicing

