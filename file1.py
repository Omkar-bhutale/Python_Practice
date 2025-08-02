import numpy as np
# lst = [1,2,3,4]
# # creating numpy array
# arr = np.array(lst)
# print(arr)
# # type of numpy array
# print(type(arr))
# # using ndim
# print(arr.ndim)
# # using len
# print(len(arr))
# # usign shape
# print(arr.shape)
# # help for function
# print(np.info(np.add))

# # tyring all
# print("Test if none of the elements of the said array is zero:")
# arr = np.array([1,2,3,4])
# print(arr,np.all(arr))
# print("Test if none of the elements of the said array is zero:")
# arr = np.array([0,2,3,4,5])
# print(arr,np.all(arr))

# # test any zero trying any
# print("Test whether any of the elements of a given array is non-zero:")
# arr = np.array([0,0,1])
# print(arr,np.any(arr))

# arr= np.array([0,0,0])
# print(arr,np.any([arr]))

# NumPy: Test a given array element-wise for finiteness (not infinity or not a Number)
# a = np.array([1, 0, np.nan, np.inf])
# #  nan-> not a number inf->infinity
# print(a,'\n',np.isfinite(a))

# print(a,'\n',np.isnan(a))
# print(a,'\n',np.isinf(a))

# NumPy: Test element-wise for complex number, real number of a given array. Also test whether a given number is a scalar type or not

# a = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])
# print("Checking for complex number:")
# print(a,'\n',np.iscomplex(a))
# print("Checking for real number:")
# print(a,'\n',np.isreal(a))
# # Checking if a value is a scalar or not (in this case, checking if 3.1 is a scalar)
# print("Checking for scalar type:")
# print(3.1,np.isscalar(3.1)) #true
# print([3.1],np.isscalar([3.1])) #false


# x = np.array([3, 5])
# y = np.array([2, 5])

# print(x>y)
# print(np.greater(x,y))
# print(x>=y)
# print(np.greater_equal(x,y))

# print(np.less(x,y))
# print(np.less_equal(x,y))

a = np.identity(3)
print(a)
# getting a random number
print(np.random.normal(0,1,1))