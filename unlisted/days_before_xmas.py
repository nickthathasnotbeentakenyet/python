import datetime
from colorama import Fore
def separator():
    return (f"{Fore.YELLOW}" + "+" + "="*40 + "+" + f"{Fore.RESET}")

today = datetime.datetime.now().date()
today_human_readable = today.strftime("%d %b, %Y")
current_year = datetime.datetime.now().date().year
xmas = datetime.date(current_year,12,25)
days_before_x = xmas - today

print(f"{separator()}\n| {Fore.CYAN}Current Date: {Fore.RED}{today_human_readable:>24}\
    \n{Fore.CYAN}| Days before X-mas: {Fore.RED}{days_before_x.days:>10}\n{separator()}")
    