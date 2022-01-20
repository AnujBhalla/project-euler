import time 
start_time = time.time()


def palindrome_tester(n):
  if str(n)[::-1] == str(n):
     return True
A=[]
for i in range(100,1000):
  for j in range(100,1000):
    if palindrome_tester(i*j) == True:
      A.append(i*j)
print(max(A))

print("--- %s s ---" % (time.time() - start_time))
