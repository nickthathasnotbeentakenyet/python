import json
import os
from datetime import datetime
import matplotlib.pyplot as plt  
from numpy import negative
import numpy_financial as npf
from colorama import Fore

AMOUNT_INDEX = 0
DATE_INDEX = 1

def main():
    print(f'{Fore.MAGENTA}-'*40+'\n'+'#'*10 +f'{Fore.RED}    SMART WALLET    '+f'{Fore.MAGENTA}#'*10+'\n'+'-'*40)
    файл_бюджета = check_create()
    exiting = False
    while not exiting:
        command = input(f"{Fore.GREEN}\n\
Главное Меню\n\
1 - доходы\n\
2 - расходы\n\
3 - калькуляторы\n\
0 - выход\n\
введите код:  \
{Fore.RESET}")
        
        match command.split():
            case ['1']: 
                while True:
                    income_command = input(f"\n{Fore.BLUE}Меню Доходов:\n1 - добавить\n2 - вывести список\n0 - выход\nвведите код: {Fore.RESET}")
                    if income_command == '1':
                        income = add_flow('Укажите источник дохода [премия, зарплата]: ')
                        write_json(файл_бюджета, income,"income")
                    elif income_command == '2':
                        все_доходы = read_budget(файл_бюджета,'income')
                        print_budget(все_доходы,'доходов')   
                    elif income_command == '0': break
                    else: print(f'{Fore.LIGHTRED_EX}Ошиблись циферкой?{Fore.RESET}')
            case ['2']:  
                while True:
                    expense_command = \
input(f"{Fore.BLUE}\nМеню Расходов:\n1 - добавить\n2 - вывести список\n3 - статистика\n0 - выход\nвведите код: {Fore.RESET}")
                    if expense_command == '1': 
                        expense = add_flow('Укажите цель расхода [еда, бензин]: ')
                        write_json(файл_бюджета, expense,"expenses")
                    elif expense_command == '2':
                        все_расходы = read_budget(файл_бюджета,'expenses')
                        print_budget(все_расходы, 'расходов')
                    elif expense_command == '3':
                        expenses = read_budget(файл_бюджета,'expenses')
                        period = int(input(f'За какой период смотрим? [7, 30, 365]: '))
                        цели, суммы = print_expenses_period(expenses, period)
                        try: 
                            create_plot(суммы, цели)
                        except: print('упс...кажется недостаточно данных')
                    elif expense_command == '0': break
                    else: print(f'{Fore.LIGHTRED_EX}Ошиблись циферкой?{Fore.RESET}')
            case ['3']:          
                while True:
                    try:
                        calculator_command = input(f"{Fore.BLUE}\nМеню Калькуляторов:\n1 - финансовая независимость\n2 - первоначальный платеж\
                            \n3 - оплата кредита\n4 - дебитовое накопление\n0 - выход\nвведите код: {Fore.RESET}")
                        if calculator_command == '1':
                            ставка = float(input("\nВведите процентную ставку [0.05]: "))
                            лет = float(input("Введите количество лет: "))
                            желаемая_сумма = float(input("Введите желаемую сумму [500000]: "))
                            result = npf.pmt(rate=ставка/12, nper=лет*12, pv=0, fv=желаемая_сумма)
                            print("="*30,f"Срок: {лет} лет\nСтавка: {ставка} %\nЖелаемая сумма: {желаемая_сумма} ₽")
                            print("-"*30,f"Ежемесячное внесение: {negative(result):.2f} ₽","="*30)
                        elif calculator_command == '2':
                            ставка = float(input("\nВведите процентную ставку [0.05]: "))
                            лет = float(input("Введите количество месяцев [3 года = 36, 5 лет = 60]: ")) / 12
                            ежегодный_платеж = float(input("Введите ежегодный платеж [0 при отсутствии платежей]: "))
                            целевая_сумма = float(input("Введите желаемую целевую сумму [100000]: "))
                            result = npf.pv(rate=ставка, nper=лет, pmt=negative(ежегодный_платеж), fv=целевая_сумма)
                            print("="*30,f"Лет: {лет}\nСтавка: {ставка} %\nЕжегодный платеж: {ежегодный_платеж} ₽\nЦелевая сумма: {целевая_сумма} ₽")
                            print("-"*30,f"Певроначальный платеж: {negative(result):.2f} ₽","="*30)
                        elif calculator_command == '3':
                            ставка = float(input("\nВведите процентную ставку [0.05]: "))
                            месяцы = float(input("Введите количество месяцев [3 года = 36, 5 лет = 60]: "))
                            текущий_долг = float(input("Введите текущее значение долга [68000]: "))
                            result = npf.pmt(rate=ставка/12, nper=месяцы, pv=текущий_долг, fv=0)
                            print("="*30,f"Срок: {месяцы} месяцев\nСтавка: {ставка} %\nТекущий долг: {текущий_долг} ₽")
                            print("-"*30,f"Ежемесячный платеж: {negative(result):.2f} ₽","="*30)
                        elif calculator_command == '4':
                            ставка = float(input("\nВведите процентную ставку [0.05]: "))
                            лет = float(input("Введите количество месяцев [3 года = 36, 5 лет = 60]: ")) / 12
                            ежегодный_платеж = float(input("Введите ежегодный платеж [0 при отсутствии платежей]: "))
                            разовый_платеж = float(input("Введите первоначальный платеж [10000]: "))
                            result = npf.fv(rate=ставка, nper=лет, pmt=negative(ежегодный_платеж), pv=negative(разовый_платеж))
                            print("="*30,f"Лет: {лет}\nСтавка: {ставка} %\nЕжегодный платеж: {ежегодный_платеж} ₽\nРазовый платеж: {разовый_платеж} ₽")
                            print("-"*30,f"Накопление: {result:.2f} ₽","="*30)
                        elif calculator_command == '0': break
                        else: 
                            print(f'{Fore.LIGHTRED_EX}Ошиблись циферкой?{Fore.RESET}')
                    except:
                        print("Ошибка. Проверьте вводимые значения.")
            case ['0']:
                print("До свидания...")
                exiting = True
            case _:
                print(f"\n{Fore.LIGHTRED_EX}Неизвестная команда {command!r}{Fore.RESET}")

# Если файла нет, создать и вписать нужные начальные данные
def check_create():
    cwd = os.getcwd()
    filename = cwd + '\\' + 'budget.json'
    if not os.path.exists('budget.json'):
        data = '{"income": [],"expenses":[]}'
        with open(filename, "w") as file:
            file.write(data)
        file.close()
    return filename

# создаем источник дохода / цель расхода
def add_flow(message):
    source_purpose = input(f'{Fore.MAGENTA}{message}')
    if source_purpose:
        amount = float(input(f'Укажите сумму для {source_purpose} [89.99]: '))
        date_stamp = str(datetime.now())
    flow = {source_purpose:[amount,date_stamp]}
    return flow

# добавляем инфу в конец соответствующего раздела 
def write_json(file, money_flow, section):
    with open(file,'r+', encoding='utf-8') as f:
        file_data = json.load(f)
        file_data[section].append(money_flow)
        f.seek(0)
        json.dump(file_data, f, indent = 4, ensure_ascii=False)
        print(f"Записано!{Fore.RESET}")

# читаем секцию из файла
def read_budget(file,section):
    with open(file,'r', encoding='utf-8') as f:
        data = json.load(f)
        return data[section]

# выводим секцию бюджета в терминал
def print_budget(budget,section):
        sum = 0
        print(f'{Fore.YELLOW}')
        for _ in budget:
            for key, value in _.items():
                sum += float(value[AMOUNT_INDEX])
                print(f'{key:<20}: ${value[AMOUNT_INDEX]}')
        print(f'\nОбщая сумма {section}: ${sum}{Fore.RESET}')

# выводим статистику расходов за период, возвращаем 2 списка: расход + цена
def print_expenses_period(expenses,period):
    итог = 0
    цели = []
    суммы = []
    for _ in expenses:
        for key, value in _.items():
            дата_расхода = value[DATE_INDEX]
            сумма_расхода = value[AMOUNT_INDEX]
            format = "%Y-%m-%d %H:%M:%S.%f"
            дата_расхода = datetime.strptime(дата_расхода, format).date()
            сегодня = datetime.now().date()
            период_фактический = (сегодня - дата_расхода).days
            if период_фактический <= period:
                цели.append(key)
                суммы.append(сумма_расхода)
                итог += сумма_расхода
                print(f'{дата_расхода} вы потратили {сумма_расхода} на {key}')
    print(f'Общая сумма расходов за {period} дней: {итог}')
    return цели,суммы

def create_plot(суммы, цели):
    отделить = []
    expensive = max(суммы)
    for _ in range(len(суммы)): 
        if суммы[_] == expensive: отделить.append(0.1)
        else: отделить.append(0)
    plt.pie(суммы, labels = цели,explode=отделить)
    plt.legend()
    fig = plt.gcf()
    fig.set_size_inches(12,6)
    fig.canvas.manager.set_window_title('Расходы')
    plt.show() 
    plt.savefig('расходы.png')

if __name__ == '__main__':
    main()



    # TODO:
    '''
    сортировка расходов в графике. Желательно сразу и ключ
    тест функции
    перевод на eng
    декорации
    exceptions
    документация
    '''