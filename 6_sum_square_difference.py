"""
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

# sum of squares
sum_of_squares = 0
for n in range(1, 101):
    sum_of_squares += (n*n)

# square of sum
sum = 0
for n in range(1, 101):
    sum += n

print(sum*sum - sum_of_squares)