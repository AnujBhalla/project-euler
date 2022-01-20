import time
start=time.time()

sum=0
for i in range(1,1001):
	sum+=i**i
D = [int(i) for i in str(sum)]
print(D[-10:])

print("--- %s s ---" % (time.time() - start))
	
