prime_count = 1
j=3
while j > 0:
  for i in range(2,j):
    if j%i==0: 
      j+=2
      break 
    elif i == j-1: 
      prime_count+=1 
      print(prime_count)
      j+=2 
  
  
  if prime_count == 10001:
	  print(j-2)
	  exit()
	
