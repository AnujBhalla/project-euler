def palindrome_check(n):
  return(str(n)[::-1] == str(n))
   
B = [i*j for i in range(100,1000) for j in range(100,1000) if palindrome_check(i*j)] 
print(max(B))


