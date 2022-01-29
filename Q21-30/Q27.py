from math import sqrt, ceil

def prime_check(n):
	if n == 1 or 0:
		return(False)
	if n == 2:
		return(True)
	else: 
		for i in range(2,ceil(sqrt(abs(n)))+1):
			if n%i==0:
				return(False)
				exit
		return(True)		
		
primes = [b for b in range(-1001,1001) if prime_check(b)==True]			
current = 0

for a in range(-1000,1000):
	for b in primes:
		n=0
		while n >=0:
			quadratic = n**2 + (a*n) + b
			if prime_check(quadratic) == True:
				n+=1
			else:
				if n-1 > current:
					current = n-1
					product = a*b
				break 
print(product)
