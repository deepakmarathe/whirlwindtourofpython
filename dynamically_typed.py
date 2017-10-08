# Variables are pointers 
# x = 4 means x is a pointer to some memory location which holds the value. 
# It is not required to declare the variables with type information or even the type of variable it points to can be different. It is called dynamic typing.

# x is an integer
x = 1
print("x is : ", x)

# x is a string
x = "Hello"
print("x is : ", x)

# x is a list
x = [1,2,3]
print("x is : ", x)

# y now points to x. updating x will modify y too, because they are pointing to the same list. 
y = x
x.append(4)
print y

# x can now point to something different but it will not affect the contents of y.
x = "something different"
print y

# number, string and other simple types are immutable
x = 10
y = x
x += 5
print("x is : ", x)
print("y is : ", y)

