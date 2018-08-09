# Načítání JSON souborů, práce se slovníky

Cílem cvičení je naučit se pracovat se složitějšími strukturami než jsou obyčejné proměnné.
V průběhu jenoduchých příkladů si vyzkoušíme načítání JSON souborů, což je jeden ze stadarních formátů pro ukládání dat na internetu.
Dále se naučíme načítat data do slovníku, datové struktury složící pro ukládání dat, souvisejících s jedním objektem.
Ukážeme si jak pracovat s polem, datovou strukturou šikovnou pro ukádání vice dat stejného typu.

# Základní datové struktury

Pojdmě se podívat na pole a slovník, což jsou dvě pokročilé datové struktury, bez kterých se neobejdeme.

## Slovníky a ukládání složítějších dat

V reálném světě se velmi často stává, že chceme modelovat jev nebo objekt, které nemá jenom jednu vlastnost, ale má jich několik.
Protože ukládání více souvisejích vlastností pomocí jednotlivých proměnných by vedlo ke zmatkům, máme pro tento účel bohatší datovou strukturu.
Ta struktura se jmenuje slovník a je obsažena prakticky v každém moderních programovacím jazyce, kde se pro ní označení `dict`, `dictionary` nebo `map`.
Abychom slovník vysvětlili nejjednošujeji jak jen to jde použijeme příklad.
Chceme popsat člověka, který má následující vlastnosti:

- měří 182 cm
- je to muž
- obvod hrudi má 93 cm
- obvod pasu má 70 cm
- váží 90 kg 
- barvu vlasů má hnědou
- barvu očí má modrou

Když budeme chtít tohoto člověka popsat v programu, pouze pomocí proměnných to půjde dost těžko.
Naštěstí máme slovník! Tak ho použijeme.
V zápisu pythonu bude ten samý člověk, zapsaný do slovníku vypadat takto:

```python
person = {
    'height': 182,
    'gender': 'male',
    'chest_diameter': 93,
    'waist_diameter': 70,
    'weight': 90,
    'hair_color': 'brown',
    'eye_color': 'blue'
}
```

Jakákoliv následná práce s ním je velmi jednoduchá.
Prostě přistupujeme k jednotlivým vlastnostem uloženým ve slovníku.

```python
# pro zjištění pohlaví
if person['gender'] == 'male':
    print('Je to muž')
else if person['gender'] == 'female':
    print('Je to žena')
else:
    print('Neni to ani muž ani žena')

# když je potřeba cokoliv změnit stačí to přepsat
# změníme bavu očí
person['eye_color'] = 'brown'

# do slovníku se dá i přidat další položka
# přidáme oblíbené zvíře
person['favorite_animal'] = 'unicorn'
# od této chvíle je ve slovníku nová položka
print(person['favorite_animal'])
```

V tuto chvíli je již jasné co slovník je a k čemu ho použít. 
Je to způsob jak svázat nejakou položku, nazývanou klíč (key), s konrétní hodnotou (value).
Použije se pro popis konkrétního jevu nebo objektu, pro který chceme uložit více informací naráz.

## Opakování se slovníkem

Pojďme v rychlosti projet co se slovníkem můžeme dělat.

### Vytváření slovníku a přidávanání položek

```python
# vytvoření prázného slovníku, pomocí přiřazení objektu slovník
d = dict()
# vytvoří prázný slovník, stejným způsobem jako výše, ale použije se zkrácený zápis 
d = {}
# vytvoří nový slovník obsahující dvě hodnoty pro dva klíče
d = {
    'key_1': "hodnota 1",
    'key_2': "hodnota_2"
}
# přidá do slovníku další klíč s hodnotou 15
d['key_3'] = 15
```

### Čtení ze slovníku a kontrola jestli v něm existuje položka

```python
# ze slovníku můžeme rovnou číst, pokud známe klíč pro položku
some_value = d['key_1']
if d['key_1'] == 'hodnota 1':
    print('A dá se rovnou použít i v podmínkách')

# když je potřeba ověřit jestli slovník obsahuje nějakou položku učenou konrétním klíčem
if 'key_1' in d:
    print('Klíč je ve slovníku')

# přes slovník se dá také pustit cyklus, který postupně projde všechny klíče v něm
for key in d:
    print(key)
    print(d[key])

# v případě, že se hodí projít zároveň klíč i s jeho hodnotou
for key, value in d.items():
    print(key, value)
```


Jak je vidět, slovník je mozný nástroj, který s námi setrval už od pradávna.
Tím myslím, nejen dobu počítačovou.
Slovníky máme od chvíle, kdy lidstvo vynalezlo písmo, a od té doby fungují stejně.
Skvělě se v nich hledá, mají jasný systém a umožnují uložit velmé množstí jasně strukturovaných informací.

### Reference

Python dokumentace: [python dict]()

## Pole a ukládání vícero dat

V praxi se velmi často stává, že je potřeba uložit více hodnot pro stejnou vlastnost.
Na příklad když chceme ukládat hodnotu teploty měřenou každé dně hodiny.
Kdybychom měli ukládat naměřené teploty do samostatných proměnných, byl by v tom za chvíli pěkný zmatek.
Ostatně posuďte sami:

```python
# teploty uložíme do 12 proměnných pro každé dvě hodiny za den
teplota_1 = 12
teplota_2 = 12
teplota_3 = 13
teplota_4 = 13
teplota_5 = 13
teplota_6 = 14
teplota_7 = 15
teplota_8 = 15
teplota_9 = 15
teplota_10 = 17
teplota_11 = 18
teplota_12 = 16

# co teď když je chci projít v cyklu?
for t in range(1,13):
    if t == 1:
        print('teplota  je', teplota_1)
    else if t == 2:
        print('teplota  je', teplota_2)
    else if t == 3:
        print('teplota  je', teplota_3)
    else if t == 4:
        print('teplota  je', teplota_4)
    else if t == 5:
        print('teplota  je', teplota_5)
    else if t == 6:
        print('teplota  je', teplota_6)
    else if t == 7:
        print('teplota  je', teplota_7)
    else if t == 8:
        print('teplota  je', teplota_8)
    else if t == 9:
        print('teplota  je', teplota_9)
    else if t == 10:
        print('teplota  je', teplota_10)
    else if t == 11:
        print('teplota  je', teplota_11)
    else if t == 12:
        print('teplota  je', teplota_12)
```

Bude to fungovat, ale je to hodně nepraktické.
Zvláště, když hodnot bude více, o hodně více.
Nebo co když budeme chtít kreslit graf?
To se dělá dost blbě, když jsou hodnoty uložené v samostatných proměnných.
Prakticky každý nástroj na kreslení grafů očekává hodnoty uložené inteligentně.

A naštěstí, stejně jako v případě slovníku, má každý programovací jazyk k dispozici datovou strukturu pro ukládání více hodnot stejného typu.
Tato struktura se jmenuje pole a je velmi intuitivní.
Toto je ten stejný příklad, ale s využitím pole.

```python
# uložení teplot do pole
teplota = [12, 12, 13, 13, 13, 14, 15, 15, 15, 17, 18, 16]

# když teď chci teplot projít
for t in teplota:
    print('teplota  je', t)
```

Elegantní, že?
Samozřejmě, že při práci s daty, není žádoucí vytvářet pole ručně, ale načítat je ze souboru, nebo jiného zdroje dat.

### Reference

Python dokumentace: [python list]()

## Slovníky a pole pro ukládání už hodně zajímavých dat

Velmi hezká vlastnost je, že pole a slovník se dají kombinovat.
Pro ilustraci si vezměme příklad, kdy budeme zpracovávat více lidí co mají nějaké vlastnosti.
Každý člověk bude mít:

- výšku,
- váhu,
- jméno,

V programu se to zapíše třeba takto:

```python
# pole do kterého uložime více lidí
persons = [
    # každý člověk je uložen jako slovník v poli
    {
        'height': 160,
        'weight': 63,
        'name': 'Jose'
    },
    {
        'height': 180,
        'weight': 92,
        'name': 'Pepe'
    },
    {
        'height': 178,
        'weight': 80,
        'name': 'Maria'
    }
]

# když budu chtít postupně vypsat všechny lidi
for person in persons:
    print(person)
```

Slovník a pole lze kombinovat i opačně.
Můžeme mít člověka, u kterého sledujeme výšku každý rok.

```python
person = {
    'name': 'Jose',
    'height': [113, 118, 124, 127]
}
```

A samozřejmě že lze kombinovat obojí naráz.

```python
persons = [
    {
        'name' = 'Jose',
        'height': [113, 118, 124, 127]
    },
    {
        'name' = 'Pepe',
        'height': [189, 192, 195, 201]
    }
]
```

Což je hodně šikovné a dává to velmi široké možnosti ukládání dat.


# JSON soubor pro ukládání dat

JSON je defacto standardní způsob ukládání dat, který v praxi potkáme hodně často.
Jedná se o textový formát, takže je čitelný a vytvořitelný přímo člověkem.
Jako příklad JSON dokumentu, se podívejme na výstup z webového stahovače novinových článků.

```json
{
    "title": "Živě: Zbývají poslední minuty. Zeman dorazil do svého štábu, Nejedlý s Mynářem už na něj čekali",
    "date": "2018-01-26 00:00:00",
    "article": "",
    "keywords": [
        "domácí",
        " Aktuálně.cz",
        " Volba prezidenta 2018",
        " Miloš Zeman",
        " Jiří Drahoš"
    ],
    "server": "aktualne_cz"
}
```

Je hezky čitelný a hned je jasné co je obsahem.
Schválně si všimněme, že JSON formát se podobá slovníku v pythonu.
A slovník v pythonu je skutečně ta datová struktura, která se použije jako zdroj nebo cíl dat při práci s JSON soubory.
Protože data mohou být leckdy velmi komplexní, umít python při načítání dat z JSON formátu využít kombinaci slovníku a pole.
Tím dostáváme velmi silný nástroj na uložení prakticky libovolného druhu dat.

V pythonu se s JSON formátem pracuje pomocí modulu `json`.

```python
import json
```

Pro načtení dat ve formátu JSON ze souboru, lze zavolat

```python
import json


with open('soubor.json') as data_source:
    data = json.load(data_source)
```

Pro uložení pak použijeme protějšek.

```python
import json

with open('soubor.json', 'w') as data_source:
    json.dump(data, data_source)
```

## Reference

Dokumantace k pythonu: [modul json](https://docs.python.org/3.6/library/json)
Dokumetace k json: [Web json](json.org)

# Cvičení pro práci s JSON formátovanými soubory

Všechny cvičení budou odevzdána formou PR.
V PR bude vždy uložen soubor s řešením, který se bude jmenovat dle šablony:

```
autor_cviceni_n.py
```

Soubory s řešením se odevzdávají do složky `results`.


## Cvičení 1 - načítání JSON souborů do pythonu

Cílem je se naučit načítat data ze souborů ve formátu JSON pythonu.
Není to nic těžkého, je to spíš takové zahřívací cvičení.

### Co mám udělat

Načíst soubor `data\aktualne_cz0.json` a celý ho vypsat.
Výpis bude postupně po jednotlivých položkách ve formátu:

```python
...
<klíč_2> : <hodnota>
<klíč_3> : <hodnota>
...
```

### Jak poznám, že to funguje

Vypíše se následující:

```python
title :  Živě: Zbývají poslední minuty. Zeman dorazil do svého štábu, Nejedlý s Mynářem už na něj čekali
date :  2018-01-26 00:00:00
article :
keywords :  ['domácí', ' Aktuálně.cz', ' Volba prezidenta 2018', ' Miloš Zeman', ' Jiří Drahoš']
server :  aktualne_cz
```


## Cvičení 2 - Spočítání počtu souborů

Toto cvičení trochu opakuje co již bylo, ale opakování matka moudrosti.
Cílem je zopakovat si práci se soubory

### Co mám udělat

Zjistit počet souborů ve složce data a vypsat ho na obrazovku.

Výpis bude ve formátu:

```python
Souboru: <n>
```

### Jak poznám, že to funguje

Vypíše se:

```python
Souboru: 1011
```


## Cvičení 3 - Nejdelší titulek

Zopakujeme si práci s proměnnými.
Úkol je najít článek s nejdelším titulkem a vypsat název souboru, ve kterém se nachází.

## Co mám udělat

Projít všechny soubory ve složce `data` a vypsat název souboru, který obsahuje nejdelší text v klíči `title`.
Když bude více souborů mít stejnou délku, vypíší se libovolný.
Výpis bude ve formátu:

```python
<delka_titulku> : <nazev_souboru>,
```

### Jak poznám, že to funguje

Vypíše se:

```python
200 : parlamentnilisty_cz303.json
```


## Cvičení 4 - Prázdný článek

Ne vždy se podaří získat data tak jak bychom chtěli.
Proto je dobré naučit se eliminovat ty vzorky, které nechceme.
Cílem toho cvičení je najít vzorky s prázným článkem a procvičit podmínky.

### Co mám udělat

Projít všechny soubory ve složce `data` a vypsat všechny soubory které v nemají článek.
To znamená, že položka `article` je prázný řetězec.
Výpis bude ve formátu:

```python
...
<nazev_souboru>
...
```

### Jak poznám, že to funguje

Vypíše se:

```python
aktualne_cz0.json
aktualne_cz1.json
aktualne_cz117.json
aktualne_cz12.json
aktualne_cz126.json
aktualne_cz127.json
aktualne_cz129.json
aktualne_cz133.json
aktualne_cz139.json
aktualne_cz142.json
aktualne_cz143.json
aktualne_cz145.json
aktualne_cz149.json
aktualne_cz155.json
aktualne_cz158.json
aktualne_cz162.json
aktualne_cz163.json
aktualne_cz169.json
aktualne_cz19.json
aktualne_cz25.json
aktualne_cz28.json
aktualne_cz3.json
aktualne_cz39.json
aktualne_cz41.json
aktualne_cz42.json
aktualne_cz45.json
aktualne_cz47.json
aktualne_cz48.json
aktualne_cz53.json
aktualne_cz6.json
aktualne_cz66.json
aktualne_cz83.json
aktualne_cz89.json
aktualne_cz91.json
ihned_cz11.json
ihned_cz14.json
ihned_cz25.json
ihned_cz72.json
ihned_cz88.json
```