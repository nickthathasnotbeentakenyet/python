import math
def compute_area_square(side):
    return side**2
def compute_area_rectangle(width, length):
    return length * width
def compute_area_circle(radius):
    return 3.14 * pow(radius,2)

loop_answer = "not quit"
while loop_answer != "quit":
    loop_answer = input("What area would you like to compute?: [square, rectangle, circle or quit to exit the program]")
    if loop_answer.lower() == "square":
        side = float(input('What is the length of a side of the square? '))
        print(f"Square Area is: {compute_area_square(side)}")
    elif loop_answer.lower() == "rectangle":
        length = float(input('What is the length of rectangle? '))
        width = float(input('What is the width of the rectangle? '))
        print(f"Rectangle Area is: {compute_area_rectangle(width, length)}")
    elif loop_answer.lower() == "circle":
        radius = float(input('What is the radius of the circle? '))
        print(f'Circle Area is: {compute_area_circle(radius)}')
else:
    print("Bye-bye..")
