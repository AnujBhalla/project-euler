from itertools import permutations as perm


def pancheck(n):
	A = [int(d) for d in str(n)]
	if len(set(A)) == len(A) == max(A) and 0 not in A:
		return(True)


pan_tuples = (perm([i for i in range(1,10)]))
pan = [int(''.join(map(str,x))) for x in pan_tuples]


def concat_product(n,tuple):
	answer = ''
	product = [n*i for i in tuple]
	for j in product:
		answer+=str(j)
	return(answer)



def max_a(a,n):
	while a>=0:
		if len(str(a*n))*n<=9:
			a+=1 
		else:
			break
		return(a)
		
print(max_a(10,50 ))	

'''for n in range(1,10):
	while a>0:
		if concat_product(a,tuple([i for i in range(1,n+1)])) not in pan:
			a+=1'''
			
			
