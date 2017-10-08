# Floating type can store fractional numbers.
# decimal notation 
# exponential notation

x = 0.000005
y = 5e-6
print x == y

x = 1400000.00
y = 1.4e6
print x == y

# float constructor can be used to convert integer to float 
a = float(1)
print a

# floating point precision is limited, can cause equality tests to be unstable
print 0.1 + 0.2 == 0.3
 
print "0.1 = {0:.17f}".format(0.1)
print "0.1 = {0:.17f}".format(0.2)
print "0.1 = {0:.17f}".format(0.3)

