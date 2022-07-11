from colorama import Fore
путь = "./продолжительность.csv"
year = input("\nВведите интересующий вас год: ")
user_country = input("Введите интересующую вас страну: ")
overall_max, overall_min = 0, 2**10
spec_year_max, spec_year_min = 0, 2**10
user_max, user_min = 0, 2**10
country_exists = False
count = 0
user_total = 0
user_count = 0
expectancy_list = []
def decor():
    print(f"{Fore.RESET}="*48)
def minidecor():
    print(f"{Fore.RESET}-"*48)
with open(путь) as file:
    file = file.readlines()
    for line in file[1:]:
        line = line.strip()
        line = line.split(",")
        # пропускаем 1ю строку / тупой метод
        # if line[3] == "Life expectancy (years)":
        #     continue
        # общие максимумы 
        if float(line[3]) > overall_max:
            overall_max = float(line[3])
            overall_country_max = line[0]
            overall_year_max = line[2]
        # общие минимумы
        if float(line[3]) < overall_min:
            overall_min = float(line[3])
            overall_country_min = line[0]
            overall_year_min = line[2]
        # инфа по конкретному году
        if line[2] == year:
            count += 1
            expectancy_list.append(line[3])
            if float(line[3]) > spec_year_max:
                spec_year_max = float(line[3])
                spec_year_country_max = line[0]
            if float(line[3]) < spec_year_min:
                spec_year_min = float(line[3])
                spec_year_country_min = line[0] 
        # инфа по конкретной стране
        if line[0] == user_country:
            country_exists = True
            user_count += 1
            user_total += float(line[3])
            if float(line[3]) > user_max:
                user_max = float(line[3])
                user_year_max = line[2]
            if float(line[3]) < user_min:
                user_min = float(line[3])
                user_year_min = line[2]
    # вычисляем сумму 
    total = 0
    for i in expectancy_list:
        total += float(i)    
    # выводим общую инфу 
    decor()
    print(f"{Fore.MAGENTA}Общая информация по всем странам и годам:")
    minidecor()
    print(f"\nМаксимальная продолжительность жизни среди всех стран: {overall_max:.2f} в {overall_country_max} в {overall_year_max}")
    print(f"Минимальная продолжительность жизни среди всех стран: {overall_min:.2f} в {overall_country_min} в {overall_year_min}\n")
    decor()
    print(f"{Fore.CYAN}Информация по интересующему вас году [{year}]:")
    minidecor()
    # предусматриваем ошибку деления на ноль
    if not expectancy_list:
        print(f"{Fore.LIGHTRED_EX}\nИнформация по этому году не найдена..\n")
    # вычисляем среднее и выводим для конкретного года
    else:    
        spec_year_average = total / count 
        print(f"\nСредняя продолжительность среди всех стран: {spec_year_average:.2f}")
        print(f"Максимальная продолжительность жизни в {spec_year_country_max} : {spec_year_max:.2f}")
        print(f"Минимальная продолжительность жизни в {spec_year_country_min} : {spec_year_min:.2f}\n")
    # выводим для конкретной страны
    decor()
    print(f"{Fore.GREEN}Информация по интересующей вас стране [{user_country}]:")
    minidecor()
    if country_exists:
        user_avg = user_total / user_count
        print(f"\nМаксимальная продолжительность жизни: {user_max:.2f} в {user_year_max}")
        print(f"Минимальная продолжительность жизни: {user_min:.2f} в {user_year_min}")
        print(f"Средняя продолжительность жизни {user_avg:.2f}\n")
    else:
        print(f"{Fore.LIGHTRED_EX}\nИзвините, информации по '{user_country}' не найдено.. \nПожалуйста, проверьте название страны.\n")    
    decor()

    '''
    Задача:
    Файл содержит информацию по продолжительности жизни (в дальнейшем ПЖ) в разных странах в разные года
    Поскольку это csv файл, то значения в нем разделены запятыми.
    Данные в файле (название и абревиатура стран) на английском языке. 
    Задание:
    1. Прочитать файл
    2. Вывести максимум и минимум для ПЖ во всех странах за все года
    3. вывести максимум, минимум и среднее для конкретного года, выбранного пользователем, по всем странам
    4. вывести максимум, минимум и среднее для конкретной страны, выбранной пользователем, по всем годам
    5. Если указанного года не существует в файле, то необходимо об этом сообщить
    6. Если указанной страны не существует в файле, то об этом надо сообщить
    Заметка для 3 и 4 пунктов: 
            максимум и минимум выводятся с указанием страны(для 3) и указанием года (для 4) и значением
            среднее выводится только со значением (поскольку все страны учавствуют в подсчете)
    '''