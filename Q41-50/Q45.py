from sympy.import solve
from sympy import Symbol
n = Symbol('n')


n = 1 
while true:
	H = n*(2*n-1)
	T = 0.5*n*(n+1)
	P = 0.5*(3*n-1)*n
	
	if type(solve(H-T,n)) == 'int' and type(solve(H-P,n))== 'int':
		print(T)
		break
	else:
		n+=1
		
	
