# -*- coding: UTF-8 -*-

# Fing the largest prime factor of the number n. 

# First I need import the necessary packages. In this case I need the squareroot, which
# I fing in the math package. I also want to work with arrays, so I import the numpy 
# package.  
import math
import numpy as np

#Setup of the problem 

n = 600851475143 
sqrt_n = math.sqrt(n)
l = []

# For loop that will provide a list of numbers that factor out of n
for i in range(int(sqrt_n)):
    a = n / (i + 1)
    if n % a == 0:
        l.append([(i + 1), a])

print(l)

g = np.array(l)

print(g)

# Now I try to run the same operation as above on the elements of the array g. 

print(g[:,1])

h = []

for x in g[:,0]:
    for i in range(int(math.sqrt(x))):
        b = x / (i + 1)
        if x % b == 0:
            h.append([(i + 1, b, x)])

print(h)

factored_factors = np.array(h)

print(factored_factors)


# This methodology worked, after I properly inspected my tables I was able to figure
# out the largest prime factor. However this does not seem to be a very elegant way of
# solving this problem. 

