i = 1
p = 3*7*11*13*17*19
while i > 0:
  count = 0
  for j in range(2,20):
    if p*i%j!=0:
      i+=1
      break
    else:
      count +=1
  if count == 18:
    print(p*i)
    exit()

