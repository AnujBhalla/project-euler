factors = []
n = int(input("enter an integer:"))
k=n
i=2
while i < k:
  if n % i == 0:
    factors.append(i)
    n = n/i 
   
  else:
    i = i+1
print(factors)
