"""
Multiples of 3 and 5
Problem 1 
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
def find_sum_of_multiples(n):
    multiples = [num for num in range(n) if num % 3 == 0 or num % 5 == 0]
    return sum(multiples)

print(find_sum_of_multiples(1000))

"""
233168
"""
