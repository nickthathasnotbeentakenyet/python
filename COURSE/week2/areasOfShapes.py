# **************************************************************************
# Core activities
import math
side = float(input('What is the length of a side of the square? '))
square = side**2
# square = math.pow(side,2)
print(f'The area of the square is: {square}')

length = float(input('What is the length of rectangle? '))
width = float(input('What is the width of the rectangle? '))
area = length * width
print('The area of the rectangle is: ' + str(area))

radius = float(input('What is the radius of the circle? ')) 
circle_area = str(3.14 * (radius**2))
print('The area of the circle is: ' + circle_area)

# **************************************************************************
print("")
# Extra activity: 
# 1

radius = float(input('What is the radius of the circle? ')) 
circle_area = str(math.pi * (radius**2))
print('The area of the circle is: ' + circle_area)

# 2
user_input = float(input('Enter value for length: '))
square_area = user_input**2
circle_area = str(math.pi * (user_input**2))
cube_volume = user_input**3
sphere_volume = round((4 / 3) * math.pi * (user_input**3),2) # the value is rounded to two decimal points
print(f'Square area: {square_area}\nCircle area: {circle_area}\nCube volume: {cube_volume}\nSphere volume: {sphere_volume}')

# 3
input_centimeters = float(input('Enter value in centimeters: '))
square_centimeters = input_centimeters**2
square_meters = (input_centimeters**2)/10000
print(f'The area of the square in centimeters is: {square_centimeters} square centimeters\nThe area of the square in meters is: {square_meters} square meters')

lenght_centimeters = float(input('What is the length of rectangle in centimeters? '))
width_centimeters = float(input('What is the width of the rectangle in centimeters? '))
area_centimeters = lenght_centimeters * width_centimeters
area_meters = area_centimeters / 10000
print('The area of the rectangle in centimeters is: ' + str(area_centimeters) + ' square centimeters\nThe area of the rectangle in meters is: ' + str(area_meters) + ' square meters')

radius_centimeters = float(input('What is the radius of the circle in centimeters? ')) 
circle_area_centimeters = math.pi * (radius_centimeters**2)
circle_area_meters = circle_area_centimeters / 10000
print('The area of the circle is: ' + str(circle_area_centimeters) + ' sq. centimeters | ' + str(circle_area_meters) + ' sq. meters')