import math

# user input
width = int(input("What is the width of the tire: "))
aspect_ratio = int(input("What is the aspect ratio: "))
wheel_diameter = int(input("What is the diameter of the wheel: "))

# calculations
volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * wheel_diameter )) / 10000000000

# output
print(f"\nThe approximate volume is {volume:.2f} liters\n")