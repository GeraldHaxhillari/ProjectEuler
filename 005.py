"""
Smallest multiple
Problem 5 
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import functools

def find_lcm(*args):
    return functools.reduce(lcm, args)

def lcm(a, b):
    return a * b // gcd(a, b)

def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)

solution = find_lcm(*range(1, 20))
print('solution: ', solution)

"""
232792560
"""
