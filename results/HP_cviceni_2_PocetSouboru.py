# Zjistit počet souborů ve složce data a vypsat ho na obrazovku.

import os

files_folder = 'C:/Users/hpavlasova/Desktop/PyMum/DictListJSON/json_files/data'

files=os.listdir(files_folder)

file_count=len(files)

print('Souboru :',file_count)
