import subprocess
import re
try:
    output = []
    clean_profiles = []
    passwd = ''
    separator = '='*20
    class colors:
        MAGENTA = '\033[95m'
        CYAN = '\033[96m'
        RED = '\033[91m'
        ENDC = '\033[0m'

    profiles = subprocess.check_output(['powershell', 'netsh wlan show profiles| Select-String "Все профили пользователей"'])
    profiles = str(profiles)
    profiles = profiles.replace('\\r','')
    profiles = profiles.replace('\\n','')
    profiles = profiles.replace("'",'')
    profiles = profiles.replace("Все профили пользователей",'')
    profiles = profiles.split(" : ")
    profiles.pop(0)
    for i in profiles:
        i = i.strip()
        clean_profiles.append(i)

    for ssid in clean_profiles:
        try:
            get_password = 'netsh wlan show profiles name="' + ssid + '" key=clear | Select-String "Содержимое ключа"'
            show_password = subprocess.check_output(['powershell', get_password])
            show_password = str(show_password)
            show_password = show_password.replace('\\r','')
            show_password = show_password.replace('\\n','')
            show_password = re.findall("[^']",show_password)
            show_password = "".join(show_password)
            show_password = show_password.split(':')
            show_password.pop(0)
            for i in show_password:
                passwd += i
            passwd = passwd.strip()
            output.append(colors.CYAN + "Имя сети: " + ssid + "\nПароль: " + passwd + "\n" + colors.MAGENTA  + colors.ENDC + separator)
        except:
            #BUG: Возможен пустой пароль. Сделать проверку на пустой пароль 
            output.append(colors.CYAN + "Имя сети: " + ssid + colors.RED + "\nПароль: не найден/ без пароля\n" + colors.ENDC + separator)
            passwd = ''

    for i in output:
        print(i)
    input("Нажмите ENTER для выхода")
except:
    input(colors.RED + "Что-то пошло не так...\n" + colors.CYAN + "Нажмите ENTER для выхода" + colors.ENDC)