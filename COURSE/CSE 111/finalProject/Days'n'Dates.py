import datetime

def main():
    # getting uer input
    # user_date = input('Enter date [YYYY-MM-DD] : ')
    user_date = '2022-08-01'
    # plitting it into lit of date object
    spl = get_date_splitted(user_date)

    YEAR = int(spl[0])
    MONTH = int(spl[1])
    DAY = int(spl[2])
    # day number of uer date
    wdnum = get_weekday_num(YEAR, MONTH, DAY)
    # weekday of uer date
    wdname = get_weekday_name(wdnum)
    print(f'Weekday is: {wdname}')


    l10 = get_ten_years(YEAR,MONTH,DAY)
    wd10 = []
    # lambda map, обччнй фор тоже работает норм
    wd10.append(str(get_weekday_name(int(_))) for _ in l10)
    print(wd10)




def get_date_splitted(date_string):
    return date_string.split('-')

def get_weekday_name(daynum):
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return day_names[daynum]

def get_weekday_num(y,m,d):
    return datetime.date(y,m,d).weekday()

def get_ten_years(y,m,d):
    l10 = []
    for _ in range(11):
        wd = str(datetime.date(y, m, d).weekday())
        l10.append(wd)
        y = y + 1
    return l10

def print_l10(wd10, year):
    print('Next 10 year: ')
    for _ in wd10:
        print(f'{year}: {_}')
        year += 1





if __name__ == '__main__':
    main()


    # NOTE: везде использовать списки, даже если 1
    