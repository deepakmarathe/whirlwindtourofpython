# Everything is an object. 
x = 4
print type(x)

x = 'hello'
print type(x)

x = 3.14
print type(x)

# Python has types. However, types are not linked to the variable names, but the object themselves. 

# objects have attributes and methods. 
x = 4.5

# real and imag are the attributes
print x.real, "+", x.imag, "i"

# is_integer() is a method.
print x.is_integer()

