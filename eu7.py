# -*- coding: UTF-8 -*-

from math import sqrt
l = []
x = 1
n = 2 

while x <= 10001:
    for d in range(2, int(sqrt(n) + 1)):
        if n % d == 0:
            n += 1
            break
    else:
        l.append(n)
        n += 1
        x += 1

print len(l)

print l[10000]
