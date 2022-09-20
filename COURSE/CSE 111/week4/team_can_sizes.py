import math

PI = math.pi

def main():
    print("#1 Picnic:" , "{:.2f}".format(compute_volume(PI, 6.83, 10.16) / compute_surface_area(PI, 6.83, 10.16)))
    print("#1 Tall: " , "{:.2f}".format(compute_volume(PI, 7.78, 11.91) / compute_surface_area(PI, 7.78, 11.91)))
    print("#2: " , "{:.2f}".format(compute_volume(PI, 8.73, 11.59) / compute_surface_area(PI, 8.73, 11.59)))
    print("#2.5: " , "{:.2f}".format(compute_volume(PI, 10.32, 11.91) / compute_surface_area(PI, 10.32, 11.91)))
    print("#3 Cylinder: " , "{:.2f}".format(compute_volume(PI, 10.79, 17.78) / compute_surface_area(PI, 10.79, 17.78)))
    print("#5: " , "{:.2f}".format(compute_volume(PI, 13.02, 14.29) / compute_surface_area(PI, 13.02, 14.29)))
    print("#6Z: " , "{:.2f}".format(compute_volume(PI, 5.40, 8.89) / compute_surface_area(PI, 5.40, 8.89)))
    print("#8Z short: " , "{:.2f}".format(compute_volume(PI, 6.83, 7.62) / compute_surface_area(PI, 6.83, 7.62)))
    print("#10: " , "{:.2f}".format(compute_volume(PI, 15.72, 17.78) / compute_surface_area(PI, 15.72, 17.78)))
    print("#211: " , "{:.2f}".format(compute_volume(PI, 6.83,12.38) / compute_surface_area(PI, 6.83,12.38)))
    print("#300: " , "{:.2f}".format(compute_volume(PI, 7.62, 11.27) / compute_surface_area(PI, 7.62, 11.27)))
    print("#303: " , "{:.2f}".format(compute_volume(PI, 8.10, 11.11) / compute_surface_area(PI, 8.10, 11.11)))

def compute_volume(PI, radius, height):
    return PI * radius ** 2 * height

def compute_surface_area(PI, radius, height):
    return 2 * PI * radius * (radius + height)

main()