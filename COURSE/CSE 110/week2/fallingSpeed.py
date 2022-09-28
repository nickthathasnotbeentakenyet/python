# v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))

import math

# # input
print("Welcome to the velocity calculator. Please enter the following: \n")
# m = float(input("Mass (in kg): "))
# g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
# p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
t = float(input("Time (in seconds): "))
# A = float(input("Cross sectional area (in m^2): "))
# C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

# # calculations
# c = (1/2) * p * A * C 
# velocity = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))

# # output
# print(f"\nThe inner value of c is: {c:.3f}")
# print(f"The velocity after {t:.1f} seconds is: {velocity:.3f} m/s")

# extra activity

radius = 4
length = 9
circle_area = math.pi * (radius**2)
cylinder = circle_area * length
c = (1/2) * 1.3 * .001 * 1.1 # in the air
velocity_earth = math.sqrt(.6 * 9.8 / c) * (1 - math.exp((-math.sqrt(.6 * 9.8 * c) / .6) * t))
velocity_jupiter = math.sqrt(.6 * 24 / c) * (1 - math.exp((-math.sqrt(.6 * 24 * c) / .6) * t))

print(f"The velocity of a loaf of bread on Earth is: {velocity_earth:.3f} m/s")
print(f"The velocity of a loaf of bread on Jupiter is: {velocity_jupiter:.3f} m/s")


