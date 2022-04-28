class colors:
    RED = '\033[91m'
    ENDC = '\033[0m'

# getting and storing input from user
child_meal_price = float(input('\nWhat is the price of a child\'s meal? '))
adult_meal_price = float(input('What is the price of an adult\'s meal? '))
children_number = int(input('How many children are there? '))
adults_number = int(input('How many adults are there? '))
tax_rate = float(input('What is the sales tax rate? '))
tip_answer = input('Would you like to give a tip? [yes/no] ').lower()
if tip_answer in ('yes', 'y'):
    tip_percentage = int(input('What is the tip percentage? '))   
else:
    tip_percentage = 0 

# making calculations
subtotal = child_meal_price * children_number + adult_meal_price * adults_number
tax = tax_rate * subtotal / 100
total = subtotal + tax
tip = total * tip_percentage / 100
total_with_tip = total + tip

# printing results
# if user pays the tip
if tip_answer in ('yes', 'y'):
    print(f'\nSubtotal: ${subtotal:.2f}')
    print(f'Sales Tax: ${tax:.2f}')
    print(f'Tip: ${tip:.2f}')
    print(f'Total: ${total_with_tip:.2f}')
#if user doesn't pay the tip    
else:
    print(f'\nSubtotal: ${subtotal:.2f}')
    print(f'Sales Tax: ${tax:.2f}')
    print(f'Total: ${total:.2f}')  

# getting input for payment amount
payment = float(input('\nWhat is the payment amount? '))

# calculating and printing the change
if tip_answer in ('yes', 'y'):
    change = payment - total_with_tip
else:
    change = payment - total    

# in case customer pays less the change is displayed in red
if change < 0:
    print('Change: ' + colors.RED + f'${change:.2f}\n' + colors.ENDC)
else:
    print(f'Change: ${change:.2f}\n')

# exit
input('Please press any button to exit...')