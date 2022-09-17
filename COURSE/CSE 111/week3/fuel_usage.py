def main():
    start_miles = float(input("An odometer value in miles: "))
    end_miles = float(input("Another odometer value in miles: "))
    amount_gallons = float(input("A fuel amount in U.S. gallons: "))
    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)
    lp100k = lp100k_from_mpg(mpg)
    print(f"{mpg:.1f} miles per gallon \n{lp100k:.2f} liters per 100 kilometers")
    # pass


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    return (end_miles - start_miles) / amount_gallons


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    return 235.215 / mpg


# Call the main function so that
# this program will start executing.
main()