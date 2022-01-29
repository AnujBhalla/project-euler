odds = [i for i in range(2,1002) if i%2==1]

count = sum( [ i**2-j*(i-1) for i in odds for j in range(4)] )

print(count)

