letter_assignment = {"0":"0","1": "3","2":"3","3":"5","4":"4","5":"4","6":"3","7":"5",
"8":"5","9":"4","10":"3","11":"6","12":"6","13":"8","14":"8","15":"7","16":"7","17":"9",
"18":"8","19":"8","20":"6","30":"6","40":"5","50":"5","60":"5","70":"7","80":"6","90":"6",}


def digit_counter(n): 
	return(len(str(n)))

def decomposer(n): 
	A=[int(d) for d in str(n)]
	Tens=[10*i for i in range(1,11)]
	if n in range(1,21) or n in Tens: #these are handled in the dictionary 
		return (n,) 
	
	elif digit_counter(n) == 2: #here we handle two digit numbers which aren't in the dictionary
		return (10*A[0],A[1])
	
	elif digit_counter(n) == 3 and n%10==0: #when we have a three digit multiple of ten we don't want to separate the tens and the units
		return (A[0],10*A[1])
	else:
		if n-100*A[0] in range(11,20): #the numbers ending in teens (and 11) are special. we don't want to decompose them in the same way
			return(A[0],10*A[1]+A[2])
		else:
			return (A[0],10*A[1],A[2])

sum = 21 #start from 21 to include contribution of 1000 and 100
for i in range(1,100):   #no 'ands' are involved here
	for j in decomposer(i):
		sum+=int(letter_assignment[str(j)])
for i in range(101,1000):
	if i%100!=0:
		for j in decomposer(i):
			sum+=int(letter_assignment[str(j)]) 
		sum+=10 #for 'and' & 'hundred'
	else:
		for j in decomposer(i):
			sum+=int(letter_assignment[str(j)])
		sum +=7 #multiples of 100 don't contain 'and' 
print(sum)

	
