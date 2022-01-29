from itertools import permutations as perm 
pan_tuples = (perm([i for i in range(0,10)]))
pan = sorted([(''.join(map(str,x))) for x in pan_tuples])
print(pan[10**6 -1 ])

