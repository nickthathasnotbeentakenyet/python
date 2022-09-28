# import
from datetime import datetime

# variables and constants
weekday = datetime.now().weekday() + 1  #I prefer Monday to be the 1st day of the week
TAX_RATE = .06

# test days
weekday = 5

# user input
subtotal = float(input("Please enter the subtotal: "))

# calculations: discount, tax, total
if (weekday == 2 or weekday == 3) and subtotal >= 50:
    discount = subtotal * 0.1
else:
    discount = 0

subtotal = subtotal - discount
tax_amount = subtotal * TAX_RATE
total = subtotal + tax_amount

# output
if discount > 0:
    print(f"Discount amount: ${discount:.2f}")
print(f"Sales tax amount: ${tax_amount:.2f}")
print(f"Total: ${total:.2f}")


