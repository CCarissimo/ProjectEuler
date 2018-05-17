# -*- coding: UTF-8 -*-

# Square of the sum

a = 0

for i in range(101):
    a = a + i

sum_squared = a ** 2 

# Sum of the squares

b = 0

for i in range(101):
    c = i ** 2
    b = b + c 

# Difference between sum of squares and square of sum 

d = sum_squared - b
print(d)