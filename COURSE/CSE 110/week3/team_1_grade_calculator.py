grade_percentage = float(input("What is the grade percentage?: "))
# passed 
if grade_percentage >= 70:
    if grade_percentage >= 90:
        letter = "A"   
    elif grade_percentage >= 80:
        letter = "B"
    else:
        letter = "C"
    print("Congratulations! You successfuly passed this course!")   
# failed
else:    
    if grade_percentage >= 60:
        letter = "D"
    else:
        letter = "F"          
    print("Sorry, looks like you did not succeed in this class.")
# ---------------------------------------------------------------
# adding sign after letter
if grade_percentage % 10 >= 7:
    sign = "+"  
elif grade_percentage % 10 < 3:
    sign = "-" 
# if last digit is between 3 and 6 - no sign added
else:
    sign = ""    
# removing sign from A+ and F
if grade_percentage >= 93 or grade_percentage < 60:
    sign = ""  
# ---------------------------------------------------------------
# printing grade and sign 
print(f"Your grade is \"{letter}{sign}\"") 
