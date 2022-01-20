from math import isqrt, ceil, sqrt, floor 
from time import time 

start = time()

i = 3

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


while True:
	max = floor(sqrt(0.5*i)) #the integer we need to check squares up to
	prime_array = [prime_check(i - 2*(n**2)) for n in range(max+1)]
	if sum(prime_array)> 0: #there is a prime inside it 
		i +=2
	else: 
		print("the answer is: " + str(i))
		break
		

print("runtime was: " + str(time()-start) + "s")

