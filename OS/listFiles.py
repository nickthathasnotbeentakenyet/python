# # поиск всех файлов по всем директориям рекурсивно
# import os 
# path = "C:/Users/warning" 
# name_list = [] 
# for root, dirs, files in os.walk(path): 
#     for file in files: 
#         name_list.append(os.path.join(root,file)) 
#         for name in name_list: 
#             print(name)

# # поиск всех файло с конкретным расширением
# import os 
# path = "C:/" 
# for root, dirs, files in os.walk(path): 
#     for file in files: 
#         if(file.endswith(".py")): 
#             print(os.path.join(root,file))

# запись в файл
import os 
# откуда читаем
path = "C:/Users/warning/Documents/" 
name_list = []
for root, dirs, files in os.walk(path): 
    for file in files: 
        # интересуют только питоновские файлы
        if(file.endswith(".py")): 
            name_list.append(os.path.join(root,file))
# куда пишем
store = "C:/Users/warning/Documents/'список файлов.txt'"
with open(store, 'w', encoding='utf-8') as f:
    for i in name_list:
        f.write(i + "\n")
f.close()


# ------------------------------ UNIX + WINDOWS
# хомяк в обеих осях
# from pathlib import Path
# p = Path('~').expanduser()
# print(p)

import os 
from pathlib import Path
# крадем из хомяка названия всех файлов
path = Path('~').expanduser() 
name_list = []
for root, dirs, files in os.walk(path): 
    for file in files: 
        # интересуют только txt файлы. 
        if(file.endswith(".txt")): 
            name_list.append(os.path.join(root,file))
# куда пишем
# файл записи находится в хомяке > документы
store = path / "Documents/'список файлов.txt'"
with open(store, 'w', encoding='utf-8') as f:
    for i in name_list:
        f.write(i + "\n")
f.close()