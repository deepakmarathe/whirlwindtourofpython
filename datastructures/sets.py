# Sets

# Unordered collection of unique elements
primes = {2, 3, 5, 7}
odds = {1, 3, 5, 7, 9}

print "primes : ", primes
print "odds : ", odds

# Union of sets
print "primes | odds : ", primes | odds
print "primes.union(odds) : ", primes.union(odds)

# Intersection using & as well as .intersection(<set>) method
print "primes & odds : ", primes & odds
print "primes.intersection(odds) : ", primes.intersection(odds)

# difference - items in one set and not the other
print "primes - odds : ", primes - odds
print "primes.difference(odds) : ", primes.difference(odds)

# symmetric difference 
print "primes ^ odds : ", primes ^ odds 
print "primes.symmetric_difference(odds) : ", primes.symmetric_difference(odds)

