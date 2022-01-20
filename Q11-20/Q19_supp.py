Normal_Year = [31,28,31,30,31,30,31,31,30,31,30,31]
Cumulative_Normal_Year = [sum(Normal_Year[:i]) for i in range(1, len(Normal_Year))]
Leap_Year = Normal_Year 
Leap_Year[1]=29
Cumulative_Leap_Year = [sum(Leap_Year[:i]) for i in range(1, len(Leap_Year))]

print(Cumulative_Normal_Year)
