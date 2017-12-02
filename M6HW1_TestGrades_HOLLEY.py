#Marcus Holley
#November 30, 2017
#CTI 110.0901
#M6HW1: Test Average & Grades

#This program asks the user to enter five test grades. These grades are matched to a letter grade and averaged.

#Assign letter grade
def letterGrade(testScore):
    if (testScore>=90):
        return "A"
    elif (testScore >=80 and testScore <90):
        return "B"
    elif (testScore >=70 and testScore <80):
    	return "C"
    elif (testScore >=60 and testScore <70):
        return "D"
    else: 
        return "F"
    
#Variables
testScoreTotal = 0 
num_Tests = 5 
    
#Tests passed into the calcAverage function
for test in range(1,num_Tests+1):  
    testScore = float(input("Please enter your score for test #{} ".format(test)))
    testScoreTotal = testScoreTotal + testScore
    print("The letter grade for your test is {} ".format(letterGrade(testScore)))


#Get Average test score and grade
def calc_Average(testScoreTotal):
    return testScoreTotal/5; 

#Show Result
print("The overall average of your test scores is: {}".format(calc_Average(testScoreTotal)))
print("The overall average letter grade for your test scores is: {} ".format(letterGrade(calc_Average(testScoreTotal)))) 


