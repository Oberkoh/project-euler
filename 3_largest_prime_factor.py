number = 600851475143

def isPrime(num):
    for n in range(2, num):
        if num%n == 0:
            return False
    return True

for n in range(2, (number//2 + 1)):
    if number%n == 0:
        if isPrime(n):
            print(n)

# TODO: Works, but fix infinte loop