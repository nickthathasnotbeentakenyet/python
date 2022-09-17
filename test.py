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
store = path / "Downloads/'список файлов.txt'"
with open(store, 'w', encoding='utf-8') as f:
    for i in name_list:
        f.write(i + "\n")
f.close()