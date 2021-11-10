time=[[3,30], [6,45]]
# hour : minute
if time[0][0]>=12: time[0][0]-=12
if time[1][0]>=12: time[1][0]-=12
hour_theta=360/12
print(abs(hour_theta*(time[0][0] + (time[0][1]/60))- hour_theta*(time[1][0] + (time[1][1]/60))))