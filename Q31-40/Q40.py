import time
start = time.time()
c = ''
i = 1
while len(c) <= 1000000:
	c = c + str(i) 
	i+=1

answer = 1
for i in range(7):
	answer *= int(c[(10**i)-1])

print(answer)
print("runtime is: " + str(time.time()-start) + "s")
