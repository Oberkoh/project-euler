"""
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""

from operator import truediv

n = 40756
triangle = []
for n in range(286, 1000):
    triangle.append(n*(n+1)/2)

pentagon = []
for n in range(166, 500):
    pentagon.append(n*(3*n-1)/2)

hexagon = []
for n in range(144, 500):
    hexagon.append(n*(2*n-1))

def Intersection(lst1, lst2):
    return set(lst1).intersection(lst2)

print(Intersection(triangle, pentagon))
# for item in pentagon:
#     if item in triangle and item in hexagon:
#         print(item)

# print(all(item in triangle for item in pentagon and hexagon))
# if elem in triangle and elem in pentagon and elem in hexagon:
    
