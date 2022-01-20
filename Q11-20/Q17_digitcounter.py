def digit_counter(n):
	D=[int(d) for d in str(n)]
	return len(D)


def decomposer(n):
	
	tens=[10,20,30,40,50,60,70,80,90,100]
	
	if n in range(1,21):
		return (n,) 
	elif n in tens:
		return (n,)
	elif digit_counter(n) == 2:
		A=[int(d) for d in str(n)]
		return (10*A[0],A[1])
	
	elif digit_counter(n) == 3 and n%10==0: #when we have a three digit multiple of ten we don't want to separate the tens and the units
		A =[int(d) for d in str(n)]
		return (A[0],10*A[1])
	else:
		A = [int(d) for d in str(n)]
		if n-100*A[0] in range(11,20): #the numbers ending in teens (and 11) are special! we don't want to decompose them in the same way
			return(A[0],10*A[1]+A[2])
		else:
			return (A[0],10*A[1],A[2])
		
letter_assignment = {
"0":"0",
"1": "3",
"2":"3",
"3":"5",
"4":"4",
"5":"4",
"6":"3",
"7":"5",
"8":"5",
"9":"4",
"10":"3",
"11":"6",
"12":"6",
"13":"8",
"14":"8",
"15":"7",
"16":"7",
"17":"9",
"18":"9",
"19":"8",
"20":"6",
"30":"6",
"40":"5",
"50":"5",
"60":"5",
"70":"7",
"80":"6",
"90":"6",
"100":"7",
"1000":"11",
"and":"3",
}
sum = 0
for j in decomposer(101):
			sum=sum+int(letter_assignment[str(j)])
sum+=10

print(sum)
print(decomposer(504))
#print(decomposer(20))
#print(decomposer(311))
#print(decomposer(313))
#print(decomposer(734))


