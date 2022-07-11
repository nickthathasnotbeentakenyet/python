import time
import os 
from tqdm import tqdm
from pathlib import Path
# ~ represents $HOME directory on both NT systems (Windows7,10,11) and UNIX-like(BSD,GNU/Linux,MacOS) 
path = Path('~').expanduser() 
name_list = []
for root, dirs, files in os.walk(path): 
    for file in files: 
        # you may change file extension or completely remove next line to search for all files
        if(file.endswith(".txt")): 
            # file names with their paths will be recorded
            name_list.append(os.path.join(root,file))
# you may change the output file by providing a different path. NOTE: path / <- is $HOME directory  
store = path / "Documents/output.txt"
with open(store, 'w', encoding='utf-8') as f:
    for i in tqdm(name_list, colour="cyan"):
        time.sleep(.0001)
        f.write(i + "\n")