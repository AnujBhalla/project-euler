from math import sqrt, ceil

def prime_check(n):
	if n == 1:
		return(False)
	if n == 2:
		return(True)
	else: 
		for i in range(2,ceil(sqrt(n))+1):
			if n%i==0:
				return(False)
				exit
	return(True)
	
	
def pancheck(n):
	A = [int(d) for d in str(n)]
	if len(set(A))  == max(A) and 0 not in A:
		return(True)


pan = []
for i in range(2143,10**7):
	if i%2==1 and pancheck(i)==True:
		pan.append(i)


current = 0
for i in pan:
	if prime_check(i)==True and i > current:
		current = i
print(current)                                                                               
		

