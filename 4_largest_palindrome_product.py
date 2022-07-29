"""
Problem 4
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

largest = 999
while largest:
    product = 999 * largest
    palindrome = str(product)
    if palindrome == palindrome[::-1]:
        print(f"999 * {largest}")
        break
    largest -= 1 

# TODO: Make it work well