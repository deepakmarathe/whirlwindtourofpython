# Flexible arguments : args and kwargs
# Arguments and Key Word arguments 

# Single * before variable means expand this as a sequece
# double ** before variable means expand this as a dictionary

def catch_all(*args, **kwargs):
	print "args : ", args
	print "kwargs : ", kwargs

catch_all(1, 2, 3, a=1, b=2)
catch_all('s', keyword = 2)


# The syntax can be used for function call as well 
inputs = (1, 2, 3)
keywords = {'pi':3.14}

catch_all(*inputs, **keywords)


