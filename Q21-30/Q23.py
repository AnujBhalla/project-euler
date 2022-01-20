from math import sqrt,ceil
import time
start_time = time.time()


def proper_divisors(n):
	divisors = {1}
	if n == 0:
		divisors = {0}
	else:
		for i in range(2,ceil(sqrt(n))+1):
			if n%i==0 and i!=n:
				divisors.add(i), divisors.add(int(n/i))
	return(divisors)
	
def abundant_sum_check(n):
	for i in range(n+1):
		if sum(proper_divisors(i))>i and sum(proper_divisors(n-i))>(n-i):
			return(True)

abundant_sum = []
for i in range(1,28125):
	print(i)
	if abundant_sum_check(i) != True:
		abundant_sum.append(i)
print(abundant_sum)
print(sum(abundant_sum))

print("--- %s s ---" % (time.time() - start_time))
