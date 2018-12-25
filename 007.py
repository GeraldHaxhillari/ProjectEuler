"""
10001st prime
Problem 7 
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import numpy as np

n = 200000
sieve = np.array([True for _ in range(n)])
sieve[0:2] = False
upper_bound = int(np.sqrt(n))

for i in range(2, upper_bound+1):
    if sieve[i]:
        j = i * i
        counter = 0
        while j < n:
            sieve[j] = False
            j = (i * i) + (counter * i)
            counter += 1

primes = np.where(sieve == True)[0]

solution = primes[10000]
print('solution: ', solution)

"""
104743
"""
