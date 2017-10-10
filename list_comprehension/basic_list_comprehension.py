# Basic list comprehension 
# expr for var in iterable

print [i for i in range(20) if i % 3 > 0]

L = []
for i in range(12):
	L.append(i ** 2)
print L

# the same can be achieved in a single line using list comprehension
print [i ** 2 for i in range(12)]


