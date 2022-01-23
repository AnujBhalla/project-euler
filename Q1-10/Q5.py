i = 1
p = 2*3*5*7*11*13*17*19
arr = []

while sum(arr) < 20:
	arr = [ (p*i)%j == 0 for j in range(1,21) ]
	i+=1 

print((i-1)*p)
		
		

		
