# import
import math
from datetime import datetime

# vars and consts
current_date = datetime.now()
PATH = "volumes.txt"
phone_number = "no phone#"

# user input
tire_width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
wheel_diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# calculations
volume = (math.pi * tire_width**2 * aspect_ratio * (tire_width * aspect_ratio + 2540 * wheel_diameter )) / 10000000000

# output volume and prompt user to buy the tires
print(f"The approximate volume is {volume:.2f} liters")
buy = input("\nWould you like to buy tires? [y/n]: ")
if buy.lower() in ("yes", "y", "yes!", "+"):
    phone_number = input("Please enter your phone number.\n\
Phone#: ")
    print(f"One of our specialist will call you at '{phone_number}' in less than a minute")

# write to file
with open(PATH, "at") as file:
    print(f"{current_date:%Y-%m-%d}, {tire_width}, {aspect_ratio}, {wheel_diameter}, {volume:.2f}, {phone_number}", file=file, sep=", ")
