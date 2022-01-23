import math
def factor_tester(n):
	count = 0 
	for i in range(1,math.ceil(math.sqrt(n))+1):
		if n%i==0:
			count+=2
	return(count)
		
A=[]
i=1
sum = 0
while factor_tester(sum) < 500:
	sum +=i
	A.append(sum)
	i+=1
	
print(A[-1])
