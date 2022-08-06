"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

import math
target = 5000
sum = 0
sieve = []
primes = []

# crude method to check if a number is prime
def isPrime(num):
    for n in range(2, num):
        if num%n == 0:
            return False
    return True

# we use the crude method to generate a sieve (Erastothenes) 
# to find all the prime numbers
for n in range(2, math.ceil(math.sqrt(target))):
    if isPrime(n):
        sieve.append(n)
        # sum += n
# print(f"sieve = {sieve}")

# using the sieve we find all primes below 2million and
# put it in the primes list
primes += sieve
for n in range(math.ceil(math.sqrt(target)), target):
    for prime in sieve:
        if n%prime == 0:
            break
    else:
        primes.append(n)
        # sum += n

# print(f"primes = {primes}")
# print(sum)
terms = 0
for prime in primes:
    terms += 1
    sum += prime
    if sum >= 1000000:
        break
    if isPrime(sum):
        print(f"sum = {sum} - term = {terms}")
    

# TODO: change the isPrime method
# Use for-else loop











# number = 10000

# def isPrime(num):
#     for n in range(2, num):
#         if num%n == 0:
#             return False
#     return True

# sum = 0
# for prime in range(2, number):
#     if isPrime(prime):
#         sum += prime
#         if isPrime(sum):
#             print(sum)