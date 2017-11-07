#Marcus Holley
#November 1, 2017
#CTI 110.0901
#M6T1



CONVERSION_FACTOR = 0.6214

def main():
    #Get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    #Display the distance converted to miles.
    show_miles(kilometers)

def show_miles(km):
    #Calculate miles.
    miles = km * CONVERSION_FACTOR

    #Display the miles.
    print(km, 'kilometers equals', miles, 'miles.')

main()
