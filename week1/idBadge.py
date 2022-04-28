print('\nPlease enter the following information:\n')
first_name = input('First name: ')
last_name = input('Last name: ')
email = input('Email address: ')
phone = input('Phone number: ')
job = input('Job title: ')
id = input('ID Number: ')
delimeter = '-'*40+'\n'
# additional work
hair = input('Hair color: ')
eyes = input('Eyes color: ')
month = input('Month started: ')
training = input('Advanced Training Completion [yes/no]: ')

print(f'\nThe ID Card is:\n{delimeter}{last_name.upper()}, {first_name.capitalize()}\n{job.title()}\nID: {id}\n\n{email.lower()}\n{phone}\n')
print(f"{'Hair: ' + hair.capitalize():<22} Eyes: {eyes.capitalize()}")
print(f"{'Month: ' + month.capitalize():<22} Training: {training.capitalize()}\n{delimeter}")