# Control flow statements : break and continue

# print odd numbers
for i in range(20):
	# check if i is even 
	if i % 2 == 0 : 
		continue
	print i

a,b = 0,1
amax = 100
L = []

# Print fibonacci
while True:
	(a, b) = (b, a+b)
	if( a > amax ) : 
		break
	L.append(a)

print L

