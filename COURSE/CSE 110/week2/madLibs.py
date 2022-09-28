# importing modules
import time
import sys
# colored i/o
class colors:
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RED = '\033[91m'
    ENDC = '\033[0m'
# prompt typed by characters
prompt = 'Please enter the following:\n\n'
for i in prompt:
    print(colors.RED + i, end='')
    sys.stdout.flush()
    time.sleep(0.1)   
# user's input stored into variables
adjective = input('Adjective: '+ colors.MAGENTA).lower()
animal = input(colors.RED + 'Animal: ' + colors.MAGENTA).lower()
exclamation = input(colors.RED + 'Exclamation: '+ colors.MAGENTA).capitalize()
verb1 = input(colors.RED + 'Verb #1: '+ colors.MAGENTA).lower()
verb2 = input(colors.RED + 'Verb #2: '+ colors.MAGENTA).lower()
verb3 = input(colors.RED + 'Verb #3: '+ colors.MAGENTA).lower()
# output story
print(colors.CYAN + f'\nYour story is:\n\nThe other day, I was really in trouble. It all started when I saw a very\n{adjective} {animal} {verb1} down the hallway. "{exclamation.lower()}!" I yelled. But all\nI could think to do was to {verb2} over and over. Miraculously,\nthat caused it to stop, but not before it tried to {verb3}\nright in front of my family.\n' + colors.ENDC) 
