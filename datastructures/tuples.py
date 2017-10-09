# Tupels 

t = (1, 2, 3)
print t

t = 1, 2, 3
print t

print "len(t) : ", len(t)
print "t[0] : ",  t[0]

# tuples are immutable 
# t[0] = 100
# t.append(4)

x = 0.125
t = x.as_integer_ratio()
print t

numerator, denominator = x.as_integer_ratio()
print numerator * 1.0 / denominator

