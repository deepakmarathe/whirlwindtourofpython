# Map and Filter iterator 

# Map
square = lambda x : x ** 2
print "-- squares --"
for i in map(square, range(10)) :  
	print i

print "-- even numbers --"
is_even = lambda x : x % 2 == 0
for i in filter(is_even, range(10)):
	print i

