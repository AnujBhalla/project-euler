import time 
start = time.time()
j = 0
while j>=0:
	if len(str(j*(9**5))) >= j:
		j+=1
	else:
		break

total = 0
for i in range(10,10**(j-1)):
	D = [int(d)**5 for d in str(i)]
	if sum(D)== i:
		total+=i
print(total)

print(time.time()-start)
