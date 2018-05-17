# -*- coding: UTF-8 -*- 

import numpy as np 

"""l = np.array([[c, c ** 2] for c in range (32)])

for x in range(32):
    for y in range(32): 
        for z in range(32):
            if (l[x,1] + l[y,1] + l[z,1]) == 1000:
                print(l[x,0] * l[y,0] * l[z,0])
                print(str(l[x,1] + l[y,1] + l[z,1]))"""


l = []

for a in range(2, 1000):
    for b in range(2, 1000):
        n = a ** 2 + b ** 2
        for c in range(2, 1000):
            if n == c ** 2:
            	if a + b + c == 1000:
                    print(a * b * c)
                    print(a)
                    print(b)
                    print(c)

