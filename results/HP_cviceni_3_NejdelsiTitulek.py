#Projít všechny soubory ve složce data a vypsat název souboru, který obsahuje nejdelší text v klíči title. 
#Když bude více souborů mít stejnou délku, vypíší se libovolný.
import json
import os

files_folder = 'C:/Users/hpavlasova/Desktop/PyMum/DictListJSON/json_files/data'

files=os.listdir(files_folder)

Seznam_komplet=[]

for f in files:

	file=os.path.join(files_folder, f)

	with open(file, 'r', encoding='utf-8') as data_source:
		data = json.load(data_source)
	
		if 'title' in data:
			#rovnou pocitam delku titulku a ukladam jen delku
			Slovnik={'title':len(data['title']), 'name':f}
	
	Seznam_komplet.append(Slovnik)

Seznam_komplet.sort(key=lambda k : k['title'])

Longest_title=Seznam_komplet[-1]

print(Longest_title['title']," :",Longest_title['name'])
