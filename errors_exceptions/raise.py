# Raise exceptions 

def fibonacci(N):
	if N < 0 : 
		raise ValueError("N must be non-negative")
	L = []
	a, b = 0, 1
	while len(L) < N : 
		a, b = b, a + b
		L.append(a)
	return L

print "fibonacci(10) : ", fibonacci(10)

#print "fibonacci(-10) : ", fibonacci(-10)

N = -10
try : 
	print "trying this : "
	print "fibonacci(N) : ", fibonacci(N)
except ValueError : 
	print "Bad value, need to do something else "


