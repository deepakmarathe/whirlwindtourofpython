# Enumerate iterators 

L = [1, 2, 3, 4, 5]

print "-- begin --"
for i in range(len(L)):
	print i, L[i]
print "-- end --"

# Instead of the above method to iterate, one can also use enumerate construct. 
print "-- begin --"
for i, val in enumerate(L) : 
	print i, val
print "-- end --"



