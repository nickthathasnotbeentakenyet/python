import math

# user input
items_quantity = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

# calculations
boxes = items_quantity / items_per_box

# output
print(f"For {items_quantity} items, packing {items_per_box} items in each box, you will need {math.ceil(boxes)} boxes.")
