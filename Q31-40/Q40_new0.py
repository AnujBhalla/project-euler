total = 1
count = 1
n=1
position = [1]
answer = 1 
while position[-1] <= 1000000:
	#print(position[-1])
	if total == 10**count:
		count +=1 
	if len(position)>1 and len(str(position[-1]))!=len(str(position[-2])):
			print(total,position[-1])
			'''print(str(total)[0])'''
			answer*=int(str(total)[0])

	total +=1
	n +=count
	position.append(n)
	
print(answer)


 
