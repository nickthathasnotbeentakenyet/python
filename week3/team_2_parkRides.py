# prompt rider to enter age and height
age = int(input("What is the age of the first rider?: ")) 
height = int(input("What is the height of the first rider?: ")) 
second_rider = input("Is there a second rider (yes/no)?: ")
# check if there is a second rider
if second_rider.lower() in ("yes", "y", "yep", "+"):
    second_rider = True
    age2 =  int(input("What is the age of the second rider?: "))
    height2 = int(input("What is the height of the second rider?: "))
else:
    second_rider = False

# no riders under 36 inches allowed
if second_rider == False and height < 36:
        allow = False
elif second_rider == True and (height < 36 or height2 < 36):
        allow = False
# riders taller than 36 inches
else:
    # single rider
    if not second_rider:
        if age >= 18 and height >= 62:
            allow = True
        else:
            allow = False
    # two riders
    else:
        if age >= 18 or age2 >= 18:
            allow = True
        else:
            allow = False   
if allow:             
    print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")    
    