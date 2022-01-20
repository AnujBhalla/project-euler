alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

alphabet_values = {alphabet[i]: i+1 for i in range(26)}

def word_value(word): #function to convert word to value
	value = 0 
	for let in word:
		value += alphabet_values[let]
		 
	return(value)
	

def triangle_number_check(x):
	power = (1+8*x)**0.5
	root = -0.5 + 0.5*power
	return( root.is_integer())




with open('p042_words.txt', 'r') as f:
	answer = 0 
	for i in f.read().split(','):
		i = i.strip('"')
		answer += triangle_number_check(word_value(i))
	print(answer ) 
		
		
		
