"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

# first 50 primes = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
#                   31, 37, 41, 43, 47, 53, 59, 61, 67, 71
#                   73, 79, 83, 89, 97, 101, 103, 107, 109, 113
#                   127, 131, 137, 139, 149, 151, 157, 163, 167, 173
#                   179, 181, 191, 193, 197, 199, 211, 223, 227, 229  
#                   233, 239, 241, 251, 257, 263, 269, 271, 277, 281
#                   283, 293, 307, 311, 313, 317, 331, 337, 347, 349

# check if no prime factors (sieve of erastothenes)
# check for first 70 primes
count = 71
n = 349
prime = []

while count <= (10001):
    if n%2 != 0 and n%3 != 0 and n%5 != 0 and n%7 != 0 and n%11 != 0 and \
        n%13 != 0 and n%17 != 0 and n%19 != 0 and n%23 != 0 and n%29 != 0 and \
            n%31 != 0 and n%37 != 0 and n%41 != 0 and n%43 != 0 and n%47 != 0 and \
                n%53 != 0 and n%59 != 0 and n%61 != 0 and n%67 != 0 and n%71 != 0 and \
                    n%73 != 0 and n%79 != 0 and n%83 != 0 and n%89 != 0 and n%97 != 0 and \
                        n%101 != 0 and n%103 != 0 and n%107 != 0 and n%109 != 0 and n%113 != 0 and \
                            n%127 != 0 and n%131 != 0 and n%137 != 0 and n%139 != 0 and n%149 != 0 and \
                                n%151 != 0 and n%157 != 0 and n%163 != 0 and n%167 != 0 and n%173 != 0 and \
                                    n%179 != 0 and n%181 != 0 and n%191 != 0 and n%193 != 0 and n%197 != 0 and \
                                        n%199 != 0 and n%211 != 0 and n%223 != 0 and n%227 != 0 and n%229 != 0 and \
                                            n%233 != 0 and n%239 != 0 and n%241 != 0 and n%251 != 0 and n%257 != 0 and \
                                                n%263 != 0 and n%269 != 0 and n%271 != 0 and n%277 != 0 and n%281 != 0 and \
                                                    n%283 != 0 and n%293 != 0 and n%307 != 0 and n%311 != 0 and n%313 != 0 and \
                                                        n%317 != 0 and n%331 != 0 and n%337 != 0 and n%347 != 0 and n%349 != 0:
        prime.append(n)
        count +=1
    n += 1
# print(prime)
print(f"10001st prime is {n-1}")