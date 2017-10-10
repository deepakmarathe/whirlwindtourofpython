# Custom exceptions

class MySpecialError(ValueError) :  
	pass

try : 
	print "do something "
	raise MySpecialError("[informative error message here]")
except MySpecialError as err :
	print "do something else "

