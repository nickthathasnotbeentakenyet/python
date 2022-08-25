# REVIEW: (netsh wlan show profiles) | Select-String "\:(.+)$"  
# FIXME: TRy using the command above to avoid manual cleaning on ssid names
# NOTE: read https://codeby.net/threads/powershell-dlja-xakera-chast-ix-voruem-soxranennye-paroli-ot-wifi.60401/ 
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

    profiles = subprocess.check_output(['powershell', 'netsh wlan show profiles| find "All User Profile"'])
    profiles = str(profiles)
    profiles = profiles.replace('\\r','')
    profiles = profiles.replace('\\n','')
    profiles = profiles.replace("'",'')
    profiles = profiles.replace("All User Profile",'')
    profiles = profiles.split(" : ")
    profiles.pop(0)
    for i in profiles:
        i = i.strip()
        clean_profiles.append(i)

    for ssid in clean_profiles:
        try:
            get_password = 'netsh wlan show profiles name="' + ssid + '" key=clear | find "Key Content"'
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
            output.append(colors.CYAN + "SSID: " + ssid + "\nPASSWORD: " + passwd + "\n" + colors.MAGENTA  + colors.ENDC + separator)
        except:
            output.append(colors.CYAN + "SSID: " + ssid + colors.RED + "\nPASSWORD: No Password/ Empty\n" + colors.ENDC + separator)
            passwd = ''

    for i in output:
        print(i)
    input("Press ENTER to exit")
except:
    input(colors.RED + "Something went wrong...\n" + colors.CYAN + "Press ENTER to exit" + colors.ENDC)