# M3LAB Debugging
# Holley

def main():
# This program takes a number grade and outputs a letter grade.

# system uses 10-point grading scale
 A_score =  90-100
 B_score =  80-89
 C_score =  70-79
 D_score =  60-69
 F_score =  0-59

score = input('Enter grade: ')
            
if 100>=90:
    print('Your grade is: A')
elif 89>=80:
    print('Your grade is: B')
elif 79>=70:
    print('Your grade is: C')
elif 69>=60:
    print('Your grade is: D')
else:
    print("Grade is below the lowest value checked.")
            
   
# program start
main()
