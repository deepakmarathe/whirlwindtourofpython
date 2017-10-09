# Boolean type 

# 2 possible values, True and False 
result = 4 < 5
print "result : ", result
print "type(result) : ", type(result)

# they are case sensitive unlike in some other languages
print True, False

# bool() constructor works on numeric types and converts to boolean values. 
print "bool(2017) : ", bool(2017)
print "bool(0) : ", bool(0)
print "bool(3.14) : ", bool(3.14)
print "bool(None) : ", bool(None)
print "bool("") : ", bool("")
print "bool('abc') : ", bool('abc')
print "bool([1, 2, 3]) : ", bool([1, 2, 3])
print "bool([]) : ", bool([])

