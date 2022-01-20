from math import sqrt, ceil
import time 
start = time.time()

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


count = 2	
for i in range(1,10**6):
	if prime_check(i)==True:
		digits = [int(d) for d in str(i)]
		for d in digits:
			if d%2==0 or d==5:
				break
		else:			
			
			rotation = str(i) 
			for j in range(len(str(i))-1):
				first = (rotation)[:1]
				rest = (rotation)[1:]
				rotation = (rest+ first)
				if prime_check(int(rotation)) == False:
					break
			else:
				count +=1	

print(count)

print("runtime was: " + str(time.time()-start) + "s")
