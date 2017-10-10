# Set comprehension 
a = { n ** 2 for n in range(12) }
print a

# set comprehension will maintain uniqueness guarantees of the set.
b = { i % 3 for i in range(1000) }
print b

# dict comprehension 
c = { n:n**2 for n in range(6) }
print c

