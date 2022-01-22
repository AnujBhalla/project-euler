from math import ceil, sqrt


def proper_divisors(n):
	divisors = {1}
	if n == 0:
		divisors = {0}
	else:
		for i in range(2,ceil(sqrt(n))+1):
			if n%i==0 and i!=n:
				divisors.add(i), divisors.add(int(n/i))
				
	return(divisors)
	
