#Marcus Holley
#November 18, 2017
#CTI 110.0901
#M5HW3 - Factorial


#Variable
numberEntered = int(input("Enter a non-negative number to find the factorial of:"))
Factorial = 1

#Calculate Factorial
while(numberEntered > 0):
    Factorial = Factorial * numberEntered
    numberEntered = numberEntered-1

#Get Results
print("The Factorial of your number is: ")
print(Factorial)
