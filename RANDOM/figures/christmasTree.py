# number = int(input("Размер елочки [например, 17]: "))
# # decreasing
# for i in range(number, -1, -1):
#     for j in range (0, i):
#         print("*",end="   ")
#     print("\n")

# for i in range(0, number):
#     for j in range (i, number):
#         print("*",end="   ")
#     print("\n")

# # increasing
# for i in range(0, number+1):
#     for j in range (0, i):
#         print("*",end="   ")
#     print("\n")

# # cristmas tree | green needles, red trunk
# from colorama import Fore
# for i in range(1, number, 2):
#     needles = '*' * i
#     print(Fore.GREEN +  needles.center(number))
# if number <= 15:
#     trunk = "*"
# else:
#     trunk = "***"
# for i in range (1, int(number/4)):
#     print(Fore.RED + str(trunk).center(number),end="\n" + Fore.RESET)

# # cristmas tree with lightbulbs
from colorama import Fore
from random import choice

try:
    size = int(input("Размер елочки [целое число]: "))
except:
    print("Ошибка. Установливаю размер по-умолчанию '17'")
    size = 17
    
lightbulbs = choice([Fore.YELLOW, Fore.CYAN, Fore.MAGENTA, Fore.BLUE, Fore.WHITE, Fore.RED])
for i in range(1, size + 1):
    print(" " * (size - i) + lightbulbs + "*" + Fore.LIGHTGREEN_EX + "*" * (i-1) + Fore.LIGHTGREEN_EX + "*" * (i - 1)+ lightbulbs + "*")
    lightbulbs = choice([Fore.YELLOW, Fore.CYAN, Fore.MAGENTA, Fore.BLUE, Fore.WHITE, Fore.LIGHTRED_EX])

if size <= 10:
    trunk = "**"
else:
    trunk = "****"

for i in range (1, int(size/2)):
    print(Fore.RED + str(trunk).center(size*2),end="\n" + Fore.RESET)