"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

# first 20 primes = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
#                   31, 37, 41, 43, 47, 53, 59, 61, 67, 71

# check if no prime factors (sieve of erastothenes)
count = 20
n = 71
prime = []

while count <= (10001 - 20):
    if n%2 != 0 and n%3 != 0 and n%5 != 0 and n%7 != 0 and n%11 != 0 and n%13 != 0 and n%17 != 0 and n%19 != 0 and n%23 != 0 and n%29 != 0 and n%31 != 0 and n%37 != 0 and n%41 != 0 and n%43 != 0 and n%47 != 0 and n%53 != 0 and n%59 != 0 and n%61 != 0 and n%67 != 0 and n%71 != 0:
        prime.append(n)
        count +=1
    n += 1
print(prime)
# print(f"10001st prime is {n-1}")