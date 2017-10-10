# Multiple return values from function

def real_imag_conjugate(val):
	return val.real, val.imag, val.conjugate()

r, i, c = real_imag_conjugate(3+4j)
print "r,  i, c : ", r, i, c
