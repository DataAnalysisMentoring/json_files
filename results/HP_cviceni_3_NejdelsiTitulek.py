#Projít všechny soubory ve složce data a vypsat název souboru, který obsahuje nejdelší text v klíči title. 
#Když bude více souborů mít stejnou délku, vypíší se libovolný.
import json
import os

files_folder = 'C:/Users/hpavlasova/Desktop/PyMum/DictListJSON/json_files/data'

files=os.listdir(files_folder)

Seznam_title=[]
Seznam_file=[]
Seznam_komplet=[]

i=-1

for f in files:

	file=os.path.join(files_folder, f)

	Seznam_file.append(f)
	i+=1

	with open(file, 'r', encoding='utf-8') as data_source:
		data = json.load(data_source)
	
		if 'title' in data:
			#rovnou pocitam delku titulku a ukladam jen delku
			Seznam_title.append(len(data['title']))
	
	Slovnik={'title':Seznam_title[i], 'name':Seznam_file[i]}
	Seznam_komplet.append(Slovnik)

Seznam_komplet.sort(key=lambda k : k['title'])

Longest_title=Seznam_komplet[-1]

print(Longest_title['title']," :",Longest_title['name'])
