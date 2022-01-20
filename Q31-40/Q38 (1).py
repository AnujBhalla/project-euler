import time 
start = time.time()

def pancheck(n): #checks if an integer is pandigital of length 9 
	A = [int(d) for d in str(n)]
	if len(set(A)) == len(A) == 9 and 0 not in A:
		return(True)


def concat_product(n,t): #defines the concatination product 
	answer = ''
	product = [n*i for i in tuple([i for i in range(1,t+1)])]
	for j in product:
		answer+=str(j)
	return(int(answer))


def max_a(n): #given an n, this tells us what value of 'a' to go up to
	a=1
	while a>=0:
		if len(str(concat_product(a,n)))<=9:
			a+=1
		else:
			return(a-1)
			
answer = 0
for n in range(2,10):
	for j in range(1,max_a(n)+1):
		t = concat_product(j,n)
		if pancheck(t)==True and t>answer:
			answer = t                                                          
		
print(answer)
print("runtime " +str(time.time()-start) + "s")
