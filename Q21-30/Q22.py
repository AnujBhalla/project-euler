import string

file = open(r"E:\Users\Anuj\Documents\p022_names.txt")
sorted_names = sorted([word.strip('""') for line in file.readlines() for word in line.split(',')])
alphabet = list(string.ascii_uppercase) 

value = []
for i in sorted_names:
	score = 0
	breakdown = [d for d in i]
	for j in breakdown:
		score+=alphabet.index(j)+1
	value.append(score)
	
final_score = 0 
for i in range(len(sorted_names)):
	final_score+=((i+1)*value[i])

print(final_score)

