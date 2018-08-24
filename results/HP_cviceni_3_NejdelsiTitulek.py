#Projít všechny soubory ve složce data a vypsat název souboru, který obsahuje nejdelší text v klíči title. 
#Když bude více souborů mít stejnou délku, vypíší se libovolný.
import json
import os

files_folder = 'C:/Users/hpavlasova/Desktop/PyMum/DictListJSON/json_files/data'

files=os.listdir(files_folder)

Seznam_title=[]
Seznam_file=[]
Seznam_komplet=[]

for f in files:

	file=os.path.join(files_folder, f)

	Seznam_file.append(f)

	with open(file, 'r', encoding='utf-8') as data_source:
		data = json.load(data_source)
	
		for key in data:
			if key=='title':
				Seznam_title.append(data[key])
	
			
for i in range(len(Seznam_title)):
	delka=len(Seznam_title[i])
	Slovnik={'title':Seznam_title[i], 'name':Seznam_file[i], 'delka':delka}
	Seznam_komplet.append(Slovnik)

Seznam_komplet.sort(key=lambda k : k['delka'])

Longest_title=Seznam_komplet[-1]
print(Longest_title['delka']," :",Longest_title['name'])
#Slovnik={}
