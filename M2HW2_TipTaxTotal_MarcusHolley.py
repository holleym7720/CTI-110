#CTI-110
#M2HW2 - Tip Tax Total
#Marcus Holley
#September 6, 2017

# Get the food charge
food_charge = float (input ('Enter the cost of your meal: '))

# Calculate the charge
tip = food_charge * .18
tax = food_charge * .07
total= food_charge + tip + tax

# Display the amounts
print ('The total tax amount will be $', format (tax, ',.2f'))
print ('The total tip amount will be $', format (tip, ',.2f'))
print ('Your total bill is $', format (total, ',.2f'))
