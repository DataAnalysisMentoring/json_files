"""
Projít všechny soubory ve složce data a vypsat název souboru, který obsahuje
 nejdelší text v klíči title. Když bude více souborů mít stejnou délku, 
 vypíší se libovolný. Výpis bude ve formátu:
<delka_titulku> : <nazev_souboru>"""

import json
import os



mydir = "C:/Users/Hesham/Desktop/git_tutorial/json_files/data"
files=os.listdir(mydir)

title_files = []



for file in files: 
	file_1=os.path.join(mydir, file)

	with open(file_1,"r",encoding= "utf_8") as zdroj_data:
		data = json.load(zdroj_data)

		if "title" in data:
			title_files.append((len(data["title"]), file)) 
		

m= max(title_files, key=lambda dvojice: dvojice[0])

verze_pro_zobrazeni=list(m)

print(verze_pro_zobrazeni[0],':',verze_pro_zobrazeni[1])