import time 
start = time.time()

def pal_tester(n):
  if str(n)[::-1] == str(n):
     return True

base_10_palis = [i for i in range(1,10**6) if pal_tester(i)==True]
		
sum = 0		
for i in base_10_palis:
	if  pal_tester(int(format(i,"b"))) == True:
		sum +=i

print(sum)
print("runtime is: " +str(time.time()-start) + "s")
