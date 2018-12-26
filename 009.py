"""
Special Pythagorean triplet
Problem 9 
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import numpy as np

def find_triplet():
    for a in range(1, 500):
        for b in range(1, 500):

            c = np.sqrt(a**2 + b**2)

            if a + b + c == 1000:
                print(f"Triplet found!")
                print(f"a: {a}, b: {b}, c: {c}")
                print(f"a + b + c = {a + b + c}")
                print(f"Product abc = {a*b*c}")
                return

find_triplet()

"""
31875000
"""
