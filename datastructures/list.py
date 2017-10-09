# List : ordered collection of elements 

x = [3, 2, 1]
print "x : ", x

print "len(x) : ", len(x)

x.append(11)
print "x : ", x

print "x + [100, 200] : ", x + [100, 200]

x.sort()
print "x.sort() : ", x


# list can contain objects of any type. Its one of the advantages of dynamic type system. quick and easy to write code.
x = [1, 'two', 3.14, [0, 3, 5]]
print "x : ", x

# list of primes 
x = [2, 3, 5, 7, 11]
print "x : ", x
print "x[0] : ", x[0]
print "x[1] : ", x[1]
print "x[-1] : ", x[-1]
print "x[-2] : ", x[-2]

# slicing is a way to access sublist instead of elements. colon indicates starting(inclusive) and ending(non-inclusive) of the subarray
print "First 3 elements x[0:3] : ", x[0:3]
print "x[:3] : ", x[:3]

print "x[-3:] : ", x[-3:]

# both the expressions are equivalent - access every 2nd element of the list
print "x[::2] : ", x[::2]
print "x[0:len(x):2] : ", x[0:len(x):2]

# print the list in reverse
print "x[0:len(x):-1] : ", x[::-1]

x[0] = 100
print x
x[1:3] = [55, 66]
print x

