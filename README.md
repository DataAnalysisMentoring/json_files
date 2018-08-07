# Načítání JSON souborů, práce se slovníky

Cílem cvičení je naučit se pracovat se složitějšími strukturami než jsou obyčejné proměnné.
V průběhu jenoduchých příkladů si vyzkoušíme načítání JSON souborů, což je jeden ze stadarních formátů pro ukládání dat na internetu.
Dále se naučíme načítat data do slovníku, datové struktury složící pro ukládání dat, souvisejících s jedním objektem.
Také si ukážeme jak se dá program rozkládat do menších logických bloků.
Těm se říká funkce a fungují samostatně, zcela nezávisle na svém okolí.

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