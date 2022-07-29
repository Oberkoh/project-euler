"""
2520 is the smallest number that can be divided by 
each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly 
divisible by all of the numbers from 1 to 20?
"""
import math

# all primes from 1 to 20 must be included in the list
def isPrime(num):
    for n in range(2, num):
        if num%n == 0:
            return False
    return True

primes = []
for prime in range(2, 20):
    if isPrime(prime):
        primes.append(prime)
# print(primes)

product = math.prod(primes)
# add more prime factors after checking divisibility below
product *= 2
product *= 3
product *= 2
product *= 2
# check which ones is not a divisible
for n in range(1, 21):
    if product%n != 0:
        print(n)

# print smallest multiple of number that is divisible by 1-20
print(product)

# TODO: This is a crude method, refactor and take off the hardcoding