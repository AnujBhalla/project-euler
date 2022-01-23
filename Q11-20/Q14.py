A=[]
for i in range(2,1000000):
	count = 2
	j=i
	while j!=1:
		if j%2==0:
			j*=0.5
			count+=1
		else:
			j=3*j+1
			count+=1
	A.append(count)
print(A.index(max(A))+2)	
