"""Projít všechny soubory ve složce data a vypsat všechny soubory které v 
nemají článek. To znamená, že položka article je prázný řetězec. Výpis
 bude ve formátu: ...
<nazev_souboru>
..."""

import json
import os



mydir = "C:/Users/Hesham/Desktop/git_tutorial/json_files/data"
files=os.listdir(mydir)


empty_files = []

for file in files: 
	file=os.path.join(mydir, file)

	with open(file, "r",encoding= "utf_8") as zdroj_data:
		data = json.load(zdroj_data)
		
		if data["article"] == "":
			empty_files.append(file)
		

for file in empty_files:
	print(file)



