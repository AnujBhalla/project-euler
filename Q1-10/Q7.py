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
			
i = 1 		
count = 0 

while count < 10001:
	if prime_check(i):
		count +=1 
	i+=1

print(i-1)
