"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

n = 100
# calculate factorial
factorial = 1
for num in range(1, n+1):
    factorial *= num

# calculate the sum
sum = 0
for num in str(factorial):
    sum += int(num)

print(sum)