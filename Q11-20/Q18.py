from itertools import product, accumulate
from operator import mul

triangle = open(r"E:\Users\Anuj\Desktop\triangle.txt")
l = []
for line in triangle:
    l.append(line.rstrip().split(' '))
for i in range(len(l)):
	for j in range(len(l[i])):
		(l[i])[j]=int((l[i])[j])

prods = []
for comb in product([False, True], repeat=len(l)-1):
    path = [0, *accumulate(comb)]
    vals = [l[i][v] for i, v in enumerate([0, *accumulate(comb)])]
    prods.append(sum(vals))
print(prods)
print(max(prods))
