# Generator expressions

g = ( n ** 2 for n in range(12) )
print g
print list(g)

# creating a generator does not build values, no memory cost. generated as and when needed

g = ( n ** 2 for n in range(12) )
for i in g:  
	print i

print "--- infinite generator ----"
from itertools import count 
for i in count():
	print i 
	if i >= 10 : break
print "--- infinite generator end ---"

factors = [2, 3, 5, 7]
G = (i for i in count() if all(i % n > 0 for n in factors))
for i in G:
	print i 
	if i > 40: break

