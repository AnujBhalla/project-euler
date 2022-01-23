recs = {}
for i in range(1,1001):
	A= []
	div = 10 
	while True:
		digit, rem = div // i , div % i
		if rem == 0:
			break
		if (digit, rem) not in A:
			A.append((digit, rem))
			div = 10 * rem
		else:
			recs[i] =  len(A[A.index((digit,rem)):]) 
			break 
		
print(max(recs, key = recs.get))

