A,n,i = [1,2],2,2


while n < 4000000:
  n = A[i-2]+A[i-1]
  i=i+1
  A.append(n)

print( sum(i for i in A[:-1] if i%2 == 0) ) 

