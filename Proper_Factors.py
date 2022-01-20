import time
import math
start_time = time.time()

def proper_divisors(n):
	divisors = {1}
	if n == 0:
		divisors = {0}
	else:
		for i in range(2,math.ceil(math.sqrt(n))+1):
			if n%i==0 and i!=n:
				divisors.add(i), divisors.add(int(n/i))
				
	return(divisors)

'''for i in range(1,200):
	print(i,proper_divisors(i))'''
	
print(proper_divisors(12400213021223410))
	
print("--- %s s ---" % (time.time() - start_time))
	
