"""
Problem 4
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

first = 999
second = 999
palindrome = False

while not palindrome and first > 99:
    product = str(first * second)
    if product == product[::-1]:
        print(f"{first * second} = {first} x {second}")
        palindrome = True
        break
    first -=1
    second = first
    while not palindrome and second > 900:
        product = str(first * second)
        if product == product[::-1]:
            print(f"{first * second} = {first} x {second}")
            palindrome = True
            break
        second -= 1