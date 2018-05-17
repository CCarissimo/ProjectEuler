import numpy as np 

number = 2**1000

string = str(number)

elements = [string[i] for i in range(len(string))]

for i in range(len(string)):
	elements[i] = int(elements[i])


print(sum(elements))