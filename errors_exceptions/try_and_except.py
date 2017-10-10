# Try and except 

try:
	print "this gets executed first"
except:
	print "this gets executed only if there is an error"


try :
	print "this gets executed first"
	x = 1 / 0
except : 
	print "something bad happened"


def safe_divide(a, b):
	try : 
		return a / b
	except ZeroDivisionError : 
		return 1E100

print "safe_divide(1, 2) : ", safe_divide(1, 2)

print "safe_divide(2, 0) : ", safe_divide(2, 0)

print "safe_divide(2, '2') : ", safe_divide(2, '2')


