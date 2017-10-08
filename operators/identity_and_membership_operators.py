# identity and membership operators
# a is b 	true if a and b are identical objects
# a is not b 	true if a and b are not identical objects
# a in b 	true if a is a member of b
# a is not b 	true if a is not a member of b 

# Identity operators

# Object identity 
a = [1,2,3]
b = [1,2,3]
print "a == b : ", a == b
print "a is b : ", a is b 
print "a is not b : ", a is not b

a = [1, 2, 3]
b = a
print "a is b : ", a is b


# Membership operators
print 1 in [1, 2, 3]
print 2 not in [1, 2, 3]
 
