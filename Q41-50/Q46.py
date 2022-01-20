from math import isqrt, ceil, sqrt

i = 1

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

primes = []


while True:
	if i % 10001 == 0:
		print(i)
	if prime_check(i) == True: 
		primes.append(i)
		i+=2
	else:
		for p in primes:
			check = 0.5*(i-p)
			#if check.is_integer() == True: 
			check = int(check)
			if isqrt(check)**2 == check: #conjecture satisftied, so move to the next i
				#print(str(i) + " check completed")  
				break
			else: #integer but not square. not satisfied, change value of p 
				continue
			
			print("the answer is: " + str(i))
			break
		
		i+=2
			
	
			
		
