"""
Sum square difference
Problem 6 
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

import numpy as np

def sum_of_squares(range_start, range_end):
    return sum(i**2 for i in range(range_start, range_end))

def square_of_sum(range_start, range_end):
    return sum(range(range_start, range_end)) ** 2

def compute_difference(range_start, range_end):
    a = sum_of_squares(range_start, range_end)
    b = square_of_sum(range_start, range_end)

    return np.abs(a - b)

print(compute_difference(1, 101))

"""
25164150
"""
