# Iterators as function arguments

print range(10)
print map(lambda x : x ** 2, range(10))

L1 = (1, 2, 3, 4)
L2 = ['a', 'b', 'c', 'd']

z = zip(L1, L2)
print z
a, b = zip(*z)
print a, b

