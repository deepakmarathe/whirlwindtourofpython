# Generators are used up after iteration. However, they can be stopped and started again.

G = (n ** 2 for n in range(12))
for i in G:
	print i
	if i > 30 : break

print "doing something"

for i in G:
	print i

