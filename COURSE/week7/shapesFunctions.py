import math
def compute_area_square(side):
    return side**2

def compute_area_rectangle(width, length):
    return length * width

def compute_area_circle(radius):
    return math.pi * pow(radius,2)

user_area = "no salgas por favor"
while user_area != "quit":
    user_area = input("What area would you like to compute?: [square, rectangle, circle or quit to exit the program] ")
    if user_area.lower() == "square":
        side = float(input('What is the length of a side of the square? '))
        print(f"Square Area is: {compute_area_square(side)}")
    elif user_area.lower() == "rectangle":
        length = float(input('What is the length of rectangle? '))
        width = float(input('What is the width of the rectangle? '))
        print(f"Rectangle Area is: {compute_area_rectangle(width, length)}")
    elif user_area.lower() == "circle":
        radius = float(input('What is the radius of the circle? '))
        print(f'Circle Area is: {compute_area_circle(radius)}')
else:
    print("Bye-bye..")

#NOTE: STRETCH STARTS HERE
# def compute_area_square(side):
#     return compute_area_rectangle(side,side)

# def compute_area(shape, value, second_value_rectangle=None):
#     if shape == "square":
#         return compute_area_square(value)
#     if shape == "rectangle":
#         return compute_area_rectangle(value, second_value_rectangle)
#     else:
#         return compute_area_circle(value)

# user_area = "no salgas por favor"
# while user_area != "quit":
#     user_area = input("What area would you like to compute?: [square, rectangle, circle or quit to exit the program]")
#     if user_area.lower() == "square":
#         side = float(input('What is the length of a side of the square? '))
#         print(f"Square Area is: {compute_area(user_area, side)}")
#     elif user_area.lower() == "rectangle":
#         length = float(input('What is the length of rectangle? '))
#         width = float(input('What is the width of the rectangle? '))
#         print(f"Rectangle Area is: {compute_area(user_area, width, length)}")
#     elif user_area.lower() == "circle":
#         radius = float(input('What is the radius of the circle? '))
#         print(f'Circle Area is: {compute_area(user_area, radius)}')
# else:
#     print("Bye-bye..")