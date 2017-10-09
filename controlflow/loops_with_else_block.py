# Loops with else block 

L = []
max = 30

for i in range(2, max):
	for factor in L:
		if i % factor == 0 :
			break
	else :
		L.append(i)

print L

