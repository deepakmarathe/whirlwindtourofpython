# Prime generator using sieve of eratosthenes method

def gen_primes(N):
	primes = set()
	for i in range(2, N):
		if all(i % p > 0 for p in primes) : 
			primes.add(i)
			yield i

print list(gen_primes(1000))
