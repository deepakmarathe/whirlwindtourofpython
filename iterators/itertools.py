
from itertools import permutations
from itertools import combinations
from itertools import product

p = permutations(range(3))
print p

c = combinations(range(4), 2)
print c

p = product('ab', range(3))
print p  

