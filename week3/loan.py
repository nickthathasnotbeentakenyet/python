print("Please rate from 1 to 10 on the following: ")
loan_size = int(input("How large is the loan?: "))
credit_history = int(input("How good is your credit history?: "))
income = int(input("How high is your income?: "))
payment = int(input("How large is your down payment?: "))

if loan_size >= 5:
    if credit_history >= 7 and income >=7:
        loan = True
    elif credit_history >= 7 or income >= 7:
        if payment >= 5:
            loan = True
        else:
            loan = False    
    else:
        loan = False
else:
    if credit_history < 4:
        loan = False
    else:
        if income >= 7 or payment >= 7:
            loan = True
        elif income >= 4 and payment >= 4:
            loan = True
        else:
            loan = False
if loan:
    print("You are eligible for a loan")
else:
    print("You are not eligible for a loan")
