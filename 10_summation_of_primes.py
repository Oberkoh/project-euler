"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math
target = 2000000
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
        sum += n
# print(f"sieve = {sieve}")

# using the sieve we find all primes below 2million and
# put it in the primes list
# primes.append(sieve)
for n in range(math.ceil(math.sqrt(target)), target):
    for prime in sieve:
        if n%prime == 0:
            break
    else:
        # primes.append(n)
        sum += n

# print(f"primes = {primes}")
print(sum)