import numpy as np


##Array From Existing Data
##numpy.asarray(a, dtype = None, order = None)

# convert list to ndarray
v = np.array([1,2,3])
c= np.asarray(v)
print(c)

# ndarray from tuple
x =(1,2,3)
b = np.asarray(x)
print(b)

##numpy.fromiter - must be iterator object. iter is used to convert to iterable object
##This function builds an ndarray object from any iterable object.
list = range(5)
it = iter(list)
print(it)

c = np.fromiter(it,dtype=float)
print(c)



