import math
prime_sum = 2
i=3
while i < 2000000:
	for j in range(2,math.ceil(math.sqrt(i))+1):
		if i%j == 0:
			i+=2
			print("i =" +str(i))
			break
		elif j == (math.ceil(math.sqrt(i))):
			prime_sum +=i
			i+=2
			print("i =" +str(i))
			print("prime_sum=" + str(prime_sum))
print(prime_sum)


 
