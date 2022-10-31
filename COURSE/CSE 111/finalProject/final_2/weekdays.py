import datetime
import matplotlib.pyplot as plt

def main():
    # getting uer input
    user_date = input('Enter date [YYYY-MM-DD] : ')
    period = int(input('Enter period of years[100]: '))
    # splitting it into a list of date objects
    spl = get_date_splitted(user_date)

    YEAR = int(spl[0])
    MONTH = int(spl[1])
    DAY = int(spl[2])

    # day number of user date
    wkd_num = get_weekday_num(YEAR, MONTH, DAY)
    # weekday of user date
    wkd_name = get_weekday_name(wkd_num)
    print(f'Weekday of the date is: {wkd_name}')
    print()
    # keep records (year, weekday) for specified period
    dict = get_period_years(YEAR,MONTH,DAY,period)
    # output table of years and corresponding weekday names
    for k, v in dict.items():
        print(f'{k} : {get_weekday_name(int(v))}')
        if str(k).endswith('9'): 
            print('\n')
    print()
    # output table of weekday names and years that match
    table = get_table(dict)
    for k, v in table.items():
        print(f'{k:<15} : {v}')
    print()
    # plot
    for k, v in table.items():
        plt.bar(str(k).capitalize(), len(v), align='center')
        plt.title(f'Weekday names for {user_date} over the last {period-1} years')
        
    fig = plt.gcf()
    fig.set_size_inches(8,3)
    fig.canvas.manager.set_window_title('Weekdays')
    plt.show()
    


def get_date_splitted(date_string):
    
    return date_string.split('-')

def get_weekday_num(y,m,d):
    
    return datetime.date(y,m,d).weekday()

def get_weekday_name(day_number):
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    return day_names[day_number]

def get_period_years(y,m,d,period):
    dict = {}
    ITERATOR = 1
    y = y - period
    for _ in range(period):
        wkd = str(datetime.date(y, m, d).weekday())
        dict[y] = wkd
        y = y + ITERATOR
    
    return dict

def get_table(dictionary):
    monday    = []
    tuesday   = []
    wednesday = []
    thursday  = []
    friday    = []
    saturday  = []
    sunday    = []
    table     = {}
    for year, day in dictionary.items():
        if   day == '0': monday.append(year)
        elif day == '1': tuesday.append(year)
        elif day == '2': wednesday.append(year)
        elif day == '3': thursday.append(year)
        elif day == '4': friday.append(year)
        elif day == '5': saturday.append(year)
        elif day == '6': sunday.append(year)

    table['monday']    = monday
    table['tuesday']   = tuesday
    table['wednesday'] = wednesday
    table['thursday']  = thursday
    table['friday']    = friday
    table['saturday']  = saturday
    table['sunday']    = sunday
    
    return table




if __name__ == '__main__':
    main()

# TODO: описание, цветной вывод, дополнить тест.функции
