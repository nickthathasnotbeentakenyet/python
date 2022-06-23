# NOTE: Progress BAR
# from time import sleep
# from tqdm import tqdm
# for i in tqdm(range(100), colour='cyan', desc='Status'):
#     ...
#     sleep(.0001)

# Альтернатива (больше вариантов баров) import progress

# NOTE: TABLES with headers
# from tabulate import tabulate
# TBBTactors = [
#     ['sheldor', 'Sheldon Cooper', 'sheldonooper@gmail.com' ],
#     ['leo','Leonard Hofstadter','leonardh@yahoo.com'],
#     ['howy','Howard Wolowitz','hw123@hotmail.com'],
#     ['raj','Rajesh "Raj" Koothrappali','raj.kooth@gmail.com']
# ]
# print(tabulate(TBBTactors,headers=['username', 'name', 'email'],tablefmt="pretty"))

# # NOTE: Coloring and formatting output
# from rich import print
# print(
#     '[red] RED [/red],'
#     '[blue] BLUE [/blue],'
#     '[bold] I am bold [/bold],'
#     '[italic] gooloogooloo [/italic]')
# print(':fire: :apple:')

# from rich.console import Console
# console = Console()
# console.print("Hello", "World!", style="bold red")
# console.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")

# NOTE: Inspect tool to show methods
# my_list = ["foo", "bar"]
# from rich import inspect
# inspect(my_list ,  methods=True)