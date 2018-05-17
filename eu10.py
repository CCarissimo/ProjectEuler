# -*- coding: UTF-8 -*-

"""import numpy as np 

l = np.array([x for x in range(2000001)])

for e in range(2000000):
    if l[e] > 1:
        for n,i in enumerate(l):
            if i % e == 0:
                l[n] = 0

print l """

import numpy as np 

l = np.array([x for x in range(2000000)])

for e in range(2000000):
    if l[e] > 1:
        for n in range(2, int(2000000 / e)):
            l[(n * e)] = 0

print l
print sum(l)