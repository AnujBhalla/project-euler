from math import ceil, sqrt 
def d(n):
  factor_sum=1
  for i in range (2,ceil(sqrt(n))):
   if n%i==0:
    factor_sum+=i+(n/i)
  return(factor_sum)
 
sum=0
for j in range (10000):
  if (j)==d(d(j)) and d(j)!=j and d(j)!=1:
      sum+=j
print (sum)
