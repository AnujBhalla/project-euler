factors = []
n , i = 600851475143, 2

while n > 1:
  if n % i == 0:
    factors.append(i)
    n = n/i 
  else:
    i = i+1
print(max(factors))










