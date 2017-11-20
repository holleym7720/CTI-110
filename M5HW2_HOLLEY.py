#Marcus Holley
#November 17, 2017
#CTI 110.0901
#M5HW2 - Running Total

#Get Variables
RunningTotal = 0
numberInput = float(input("Please enter your first number or enter a negative number to quit: "))

#Calculate Running Total
while numberInput > -1:
    RunningTotal = RunningTotal + numberInput
    numberInput = float(input("Please enter the next number or enter a negative number to quit: "))

print("\nThe total value of your entered numbers is ", RunningTotal)
