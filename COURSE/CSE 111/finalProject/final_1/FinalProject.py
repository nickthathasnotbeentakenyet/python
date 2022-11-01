import os
import time
from pathlib import Path
from colorama import Fore
from tqdm import tqdm

CURRENT_DIR = os.getcwd()

def main():
    try: 
        f_list_name =  "source.txt"
        lookup_dir = CURRENT_DIR + "\SOURCE"
        placement_dir = CURRENT_DIR + "\DESTINATION"
    
        print(f"{Fore.YELLOW}Searching for files in source directory...")
        f_list = read_filenames(lookup_dir)
        count_f_source = count_files(f_list)
        print(f"{Fore.CYAN}Source dir: {count_f_source} files")
        make_filetype_folder(placement_dir)
        make_storage_file(placement_dir, f_list_name, f_list)
        move_files(f_list)
        for i in tqdm(range(count_f_source), colour='cyan', desc='Moving'):
            time.sleep(.001)
        print(f"{Fore.GREEN}Success! Files moved to their destionation folders")
        moved_files = read_filenames(placement_dir)
        make_storage_file(placement_dir, 'destination.txt', moved_files)
        print(f"{Fore.YELLOW}Removing temp files...")
        time.sleep(.5)
        remove_temp_files(placement_dir)
        files_after_cleanup = read_filenames(placement_dir)
        count_f_destination = count_files(files_after_cleanup)
        print(f"{Fore.CYAN}Destion dir: {count_f_destination} files")
        print(f"{Fore.CYAN}To view the log refer to {placement_dir}\\log.txt")
        user_answer = input(f"{Fore.MAGENTA}Move all files back to source directory? [y/n]: ")
        if get_user_answer(user_answer) == True:
            move_back_files = read_filenames(placement_dir)
            move_back(move_back_files)
            moved_back_list = read_filenames(lookup_dir)
            count_moved_back = count_files(moved_back_list)
            for i in tqdm(range(count_moved_back), colour='cyan', desc='Moving'):
                time.sleep(.001)
            print(f"{Fore.CYAN}{count_moved_back} files moved back")
            print(f"{Fore.GREEN}Files successfuly moved back to source folder")
            clear_destination(placement_dir)
            print(f"{Fore.GREEN}All temporary folders removed")
            print(f"{Fore.GREEN}Log file removed")
        print(f"{Fore.MAGENTA}Thank you for using 'File Mover'{Fore.RESET}")
    except FileNotFoundError as not_found_err:
        print(type(not_found_err).__name__, not_found_err, sep=": ")

    except PermissionError as perm_err:
        print(type(perm_err).__name__, perm_err, sep=": ")

    except Exception as excep:
        print('Please contact Arkadii Lantukh and tell him he needs to fix this. Lol')
        print(type(excep).__name__, excep, sep=": ")


def make_filetype_folder(placement_dir):
    folders = ['audio','video','images','docs','unsorted']
    for _ in folders:
        folder = placement_dir + '\\' + _
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"{Fore.YELLOW}Creating folder '{_}'")
            time.sleep(1)
        else: print(f'{Fore.LIGHTRED_EX}Required folder already exist. Skipping..')

def read_filenames(location):
    name_list = []
    for root, dirs, files in os.walk(location): 
        for file in files: 
                name_list.append(os.path.join(root,file))
    return name_list

def make_storage_file(path, f_list_name, f_list):
    time.sleep(2)
    store = path + '/' + f_list_name
    with open(store, 'w', encoding='utf-8') as f:
        for _ in f_list:
            f.write(_ + "\n")
    f.close()

def move_files(files):
    docF = ['.txt','.csv','.doc','.rtf','.xls']
    audioF = ['.wma','.mp3','.wav','m4a','.cda']
    videoF = ['.avi','.mkv','.mp4','.webm','.wmv']
    imageF = ['.gif','.jpeg','.pdf','.png','.svg']
    log_file = CURRENT_DIR + "\DESTINATION" + "\\log.txt"
    with open(log_file, 'w', encoding='utf-8') as log:
        for f in files:
            if any(f.endswith(_) for _ in docF):
                f_path = str(f).replace('SOURCE', 'DESTINATION\\docs')
            elif any(f.endswith(_) for _ in audioF):
                f_path = str(f).replace('SOURCE', 'DESTINATION\\audio')
            elif any(f.endswith(_) for _ in videoF):
                f_path = str(f).replace('SOURCE', 'DESTINATION\\video')
            elif any(f.endswith(_) for _ in imageF):
                f_path = str(f).replace('SOURCE', 'DESTINATION\\images')
            else:
                f_path = str(f).replace('SOURCE', 'DESTINATION\\unsorted')
            log.write(f + " -> " + f_path + "\n")
            os.replace(f, f_path)
    log.close()

def move_back(files):
    for f in files:
        old_loc = f
        f = str(f).split('\\') 
        f.pop(-2)
        f = '\\'.join(f)
        new_loc = str(f).replace('DESTINATION', 'SOURCE' )
        os.replace(old_loc, new_loc)
    os.remove(CURRENT_DIR + '\log.txt')

def remove_temp_files(placement_dir):
    sFile = placement_dir + "\\source.txt"
    dFile = placement_dir + "\\destination.txt"
    os.remove(sFile)
    os.remove(dFile)

def clear_destination(placement_dir):
    folders = ['audio','video','images','docs','unsorted']
    for _ in folders:
        folder = placement_dir + '\\' + _
        if os.path.exists(folder):
            os.rmdir(folder)
            print(f"{Fore.YELLOW}Removing folder '{_}'")
            time.sleep(.5)

def get_user_answer(answer):
    if str(answer).lower() in ['y', 'yes', '+', ""]: return True
    else: return False

def count_files(file_list):
    count = 0
    for _ in file_list: count += 1
    return count

if __name__ == '__main__':
    main()






# TODO: 

# Add error handling - проверить на все исключения, добавить цветной вывод
# Add comments
# Add documentation





