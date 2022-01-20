import time 
start = time.time()

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
			

num = 0
sum = 0 
i =  11
forbidden = ['0','2','4','6','8','5']
first = ['2','3''5','7']

while num <= 10:
	for letter in forbidden:
		if letter in str(i)[1:]:
			break
		if str(i)[0] not in first:
			break
	i +=2
	if prime_check(i) == True:
		t = i
		r = i 
		for j in range(len(str(i))-1):
			left = (str(r)[:-1])
			right = (str(t)[1:])
			if prime_check(int(left)) == False or prime_check(int(right))== False:
				break
			else:
				r = left
				t = right
			if j == len(str(i))-2:
				num += 1
				sum += i 
			
print(sum)
print("runtime was: " + str(time.time()-start) + "s")

