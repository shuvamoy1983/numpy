import numpy as np

## to get a list of values of values
v = np.arange(25)
print(v)

## To form a matrix with reshape
r =v.reshape(5,5)
print(r)

##the number of axes (dimensions) of the array.
print(r.ndim)

## To see the dimensions of the array. shape will be (n,m)
print(r.shape)

## an object describing the type of the elements in the array.
print(r.dtype)

## the size in bytes of each element of the array. one of type complex64 has itemsize 4 (=64/8).
print("itemsize",r.itemsize)

## the total number of elements of the array.
print(r.size)

## Array Creation
print("_____________________________________")
print("Array creation")
b = np.array([1.1,2.3,4.5])
print(b.dtype)

print("Array creation for two dimentional array and minimum dimention 2")
d = np.array([(1,2,3),(4,6,7)],ndmin=2)

## to create complex data , use dtype = complex
c = np.array([(1,2,3),(4,6,7)], dtype=complex)
print(c)
print(d)

## to print zero value in matrix
c = np.zeros((5,5))
print(c)

g = np.zeros((3,3), dtype = [('x', 'i4'), ('y', 'i4')])
print("Custom type" ,g)

##numpy.Empty-It creates an uninitialized array of specified shape and dtype.
d = np.empty([4,3],dtype=int)
print(d)
