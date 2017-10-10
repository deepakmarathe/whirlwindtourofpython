# Accessing error message

try : 
	x = 1 / 0
except ZeroDivisionError as err : 
	print "error class is : ", type(err)
	print "error message is : ", err

