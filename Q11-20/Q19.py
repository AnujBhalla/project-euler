def leap_tester(n):
	if n%400==0:
		return(True)
	elif n%4==0 and n%100!=0:
		return(True)

Normal_Year = [31,28,31,30,31,30,31,31,30,31,30,31]
Cumulative_Normal_Year = [sum(Normal_Year[:i]) for i in range(1,12)]
Leap_Year = Normal_Year 
Leap_Year[1]=29
Cumulative_Leap_Year = [sum(Leap_Year[:i]) for i in range(1,12)]

#1st Jan 1901 is a Tues. So first Sun of century is 6th jan 1901

initial = 6 #first sunday is 6th day of 1901 
count = 0 

for year in range(1901,2001): #loop through years 
	if leap_tester(year):
		days = 366
		Months = Leap_Year
		Cum_Months = Cumulative_Leap_Year
	else:
		days = 365
		Months = Normal_Year
		Cum_Months = Cumulative_Normal_Year
	for j in range(1,days+1): #loop through days in the year 
		if (j%7 == initial%7) and (j-1 in Cum_Months or j==1): 
			count +=1
	if (initial == 1 and days ==365) or (initial==2 and days == 366):
		initial = 7
	elif initial == 1 and days ==366:
		initial = 6 
	else:
		initial = (initial - days%7)%7
print(count)		
		

