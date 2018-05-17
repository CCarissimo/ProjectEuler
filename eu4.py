# -*- coding: UTF-8 -*-

def pal(num):
    return str(num) == str(num)[::-1]

maxpal = 0
for a in range(999, 99, -1):
    for b in range(a, 99, -1):
        prod = a * b 
        if pal(prod) and prod > maxpal:
            maxpal = prod

print maxpal 



