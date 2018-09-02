"""
Projít všechny soubory ve složce data a vypsat název souboru, který obsahuje
 nejdelší text v klíči title. Když bude více souborů mít stejnou délku, 
 vypíší se libovolný. Výpis bude ve formátu:
<delka_titulku> : <nazev_souboru>"""

import json
import os



mydir = "C:/Users/Hesham/Desktop/git_tutorial/json_files/data"
files=os.listdir(mydir)


empty_files = []

for file in files: 
	file=os.path.join(mydir, file)

	with open(files, "r",encoding= "utf_8") as zdroj_data:
		data = json.load(zdroj_data)


