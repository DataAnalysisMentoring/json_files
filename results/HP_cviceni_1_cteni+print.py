# Načíst soubor data\aktualne_cz0.json a celý ho vypsat. Výpis bude postupně po jednotlivých položkách ve formátu

import json
import os

files_folder = 'C:/Users/hpavlasova/Desktop/PyMum/DictListJSON/json_files/data'
soubor='aktualne_cz0.json'

file=os.path.join(files_folder, soubor)

with open(file, 'r', encoding='utf-8') as data_source:
    data = json.load(data_source)

for key in data:
	print(key,' : ',data[key])

print(data)