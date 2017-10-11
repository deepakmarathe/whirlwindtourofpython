# Numpy : Numerical Python

import numpy as np

x = np.arange(1,10)
print x

print x ** 2
print [i ** 2 for i in range(1, 10)]

print x.reshape((3,3))
print x.reshape((3,3)).T

print np.dot(x.reshape(3,3), [5, 6, 7])

print np.linalg.eigvals(x.reshape(3,3))

M = x.reshape((3,3))
print "M : ", M
