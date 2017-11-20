#Marcus Holley
#November 17, 2017
#CTI 110.0901
#M5HW1-Distance Traveled


#Get Variables
speed = int(input("Enter vehicle speed in mph: "))
time = int(input("Enter number of hours vehicle traveled: "))


#Calculations
print("hour","distance")
for hour in range(1, time + 1):
    distance = speed * hour
    print(hour,distance)
