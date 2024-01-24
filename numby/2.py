import numpy as np

array1 = np.array([1 , 10.3 , 3.25 , 0] , dtype=int) # int or 'int' or 'i'
array2 = np.array([1 , 10.3 , 3.25 , 0] , dtype=float)
array3 = array1.astype('bool')


# print(f'{array1} , {array2} , {array3} , data type : {array1.dtype}')


arr1 = np.array([ [2,3] , [4,5] , [4,5]])
arr2 = np.array([ [6,7] , [9,5] , [9,5]])

print('sum : ' , arr1 + arr2)
print('sub : ' , arr1 - arr2)
print('mult: ' , arr1 * arr2)
print('divid:' , arr1 / arr2)
print('min : ' , arr1.min())
print('max : ' , arr1.max())
print('sum : ' , arr1.sum())
print('dimension : ' , arr1.ndim)
print('ravel : ' , arr1.ravel())
print('shap rows and col : ' , arr1.shape )
print('reshap change col and rows : ' , arr1.reshape(2 , 3) )