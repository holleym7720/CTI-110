#CTI 110
#Marcus Holley
#24SEPT17
#M3HW1: Software Sales

NumberOfPackages = int(input( "Enter the number of packages Bought:"))

packagePrice = 99

if NumberOfPackages <10:
    discount = 0
elif NumberOfPackages <20:
    discount = 0.10
elif NumberOfPackages <50:
    discount = 0.20
elif NumberOfPackages <100:
    discount = 0.30
else:
    discount = 0.40

SubTotal = NumberOfPackages * packagePrice 
discountAmount = discount * subTotal 
Total= SubTotal - discountAmount


print( "Amount of Discount: $" + format( discountAmount, ",.2f" ) + "\nTotal amount: $" + format( Total, ",.2f"))
       
