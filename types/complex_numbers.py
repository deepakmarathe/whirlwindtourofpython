# complex numbers

# complext can be used to construct a complex number
x = complex(1,2)
print x

# j can be suffixed to imaginary part to represent a complex number
x = 3 + 4j
print x

# real, imag are attributes of complex numbers. 
print "x.real : ", x.real
print "x.imag : ", x.imag

# conjugate() is a method on complex numbers
print "x.conjugate() : ", x.conjugate()

# abs function works on complex numbers sqrt(x.real ** 2 + x.imag ** 2)
print "abs(x) : ", abs(x)
