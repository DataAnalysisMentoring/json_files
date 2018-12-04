#Projít všechny soubory ve složce data a vypsat všechny soubory které v nemají článek. 
#To znamená, že položka article je prázný řetězec

import json
import os
import pprint

files_folder = 'C:/Users/hpavlasova/Desktop/PyMum/DictListJSON/json_files/data'

files=os.listdir(files_folder)

Seznam_Prazdne=[]

for f in files:

	file=os.path.join(files_folder, f)

	with open(file, 'r', encoding='utf-8') as data_source:
		data = json.load(data_source)
	
		for key in data:
			if key=='article':
				if data[key]=="":
					Seznam_Prazdne.append(f)

for soubor in Seznam_Prazdne:
	print(soubor)