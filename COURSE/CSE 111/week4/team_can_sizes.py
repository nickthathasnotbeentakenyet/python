# import math

# PI = math.pi

# def main():
#     print("#1 Picnic:" , "{:.2f}".format(compute_volume(PI, 6.83, 10.16) / compute_surface_area(PI, 6.83, 10.16)))
#     print("#1 Tall: " , "{:.2f}".format(compute_volume(PI, 7.78, 11.91) / compute_surface_area(PI, 7.78, 11.91)))
#     print("#2: " , "{:.2f}".format(compute_volume(PI, 8.73, 11.59) / compute_surface_area(PI, 8.73, 11.59)))
#     print("#2.5: " , "{:.2f}".format(compute_volume(PI, 10.32, 11.91) / compute_surface_area(PI, 10.32, 11.91)))
#     print("#3 Cylinder: " , "{:.2f}".format(compute_volume(PI, 10.79, 17.78) / compute_surface_area(PI, 10.79, 17.78)))
#     print("#5: " , "{:.2f}".format(compute_volume(PI, 13.02, 14.29) / compute_surface_area(PI, 13.02, 14.29)))
#     print("#6Z: " , "{:.2f}".format(compute_volume(PI, 5.40, 8.89) / compute_surface_area(PI, 5.40, 8.89)))
#     print("#8Z short: " , "{:.2f}".format(compute_volume(PI, 6.83, 7.62) / compute_surface_area(PI, 6.83, 7.62)))
#     print("#10: " , "{:.2f}".format(compute_volume(PI, 15.72, 17.78) / compute_surface_area(PI, 15.72, 17.78)))
#     print("#211: " , "{:.2f}".format(compute_volume(PI, 6.83,12.38) / compute_surface_area(PI, 6.83,12.38)))
#     print("#300: " , "{:.2f}".format(compute_volume(PI, 7.62, 11.27) / compute_surface_area(PI, 7.62, 11.27)))
#     print("#303: " , "{:.2f}".format(compute_volume(PI, 8.10, 11.11) / compute_surface_area(PI, 8.10, 11.11)))

# def compute_volume(PI, radius, height):
#     return PI * radius ** 2 * height

# def compute_surface_area(PI, radius, height):
#     return 2 * PI * radius * (radius + height)

# main()






# STRETCH ----------------------------------------------------


# import math

# PI = math.pi

# def main():
#     print("#1 Picnic:", compute_storage_efficiency(PI,6.83, 10.16), "| Cost officiency:", round(compute_cost_efficiency(PI, 6.83, 10.16, 0.28),2))
#     print("#1 Tall:", compute_storage_efficiency(PI,7.78, 11.91), "| Cost officiency:", round(compute_cost_efficiency(PI, 7.78, 11.91, 0.43),2))
# def compute_volume(PI, radius, height):
#     return PI * radius ** 2 * height

# def compute_surface_area(PI, radius, height):
#     return 2 * PI * radius * (radius + height)

# def compute_storage_efficiency(PI, radius, height):
#     return "{:.2f}".format(compute_volume(PI, radius, height) / compute_surface_area(PI, radius, height))

# def compute_cost_efficiency(PI, radius, height, cost):
#     return compute_volume(PI, radius, height) / cost

# main()




# STRETCH LOOPS ---------------------------------------------------

import math

PI = math.pi

def main():
    cans_list = [
                # Name Radius Height Cost
                ["#1 Picnic", 6.83, 10.16, 0.28],
                ["1 Tall", 7.78, 11.91, 0.43],
                ["2", 8.73, 11.59, 0.45],
                ["2.5", 10.32, 11.91, 0.61],
                ["3 Cylinder", 10.79, 17.78, 0.86],
                ["5", 13.02, 14.29, 0.83],
                ["6Z", 5.40, 8.89, 0.22],
                ["8Z short", 6.83, 7.62, 0.26],
                ["10", 15.72, 17.78, 1.53],
                ["211", 6.83, 12.38, 0.34],
                ["300", 7.62, 11.27, 0.38],
                ["303", 8.10, 11.11, 0.42],
                ]
    bse, bce = 0, 0
    
    for line in cans_list:
        print(f"\
{line[0]:<12} \
{compute_storage_efficiency(PI, line[1], line[2]):<8} \
{compute_cost_efficiency(PI, line[1], line[2], line[3]):<8}")
        if float(compute_storage_efficiency(PI, line[1], line[2])) > float(bse):
            bse = compute_storage_efficiency(PI, line[1], line[2])
            bse_name = line[0]
        if compute_cost_efficiency(PI, line[1], line[2], line[3]) > bce:
            bce = compute_cost_efficiency(PI, line[1], line[2], line[3])
            bce_name = line[0]
    print(f"Best storage officiency: [{bse_name}] : {bse}\n\
Best cost efficiency: [{bce_name}] : {bce} \
")

def compute_volume(PI, radius, height):
    return PI * radius ** 2 * height

def compute_surface_area(PI, radius, height):
    return 2 * PI * radius * (radius + height)

def compute_storage_efficiency(PI, radius, height):
    return "{:.2f}".format(compute_volume(PI, radius, height) / compute_surface_area(PI, radius, height))

def compute_cost_efficiency(PI, radius, height, cost):
    return round(compute_volume(PI, radius, height) / cost, 2)

main()