# Generator functions and the yield

# We have 2 ways of creating a list.  
L1 = [ i ** 2 for i in range(12) ]
L2 = []
for i in range(12):
	L2.append(i ** 2)

print L1
print L2
	
# same way, we have 2 ways of creating generators. 
G1 = ( i ** 2 for i in range(12) )

def gen():
	for i in range(12):
		yield i ** 2
	
G2 = gen()

print list(G1)
print list(G2)

