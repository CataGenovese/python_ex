 Nivell 1 — Bàsic
## Exercici 1 — Escriure en un fitxer

Crea un programa que:

Obri un fitxer anomenat salutacio.txt
Escrigui:
Hola
Benvingut al tema de fitxers
Tanqui el fitxer


## Exercici 2 — Llegir un fitxer línia per línia

Utilitza el fitxer salutacio.txt de l’exercici anterior i:

Llegeix el contingut línia per línia

Mostra:

Linia 1: Hola
Linia 2: Benvingut al tema de fitxers
## Exercici 3 — Afegir text a un fitxer

Fes un programa que:

Obri salutacio.txt en mode append

Afegeixi:

Aquesta és una nova línia
Mostri després tot el contingut del fitxer
🟡 Nivell 2 — Intermedi
## Exercici 4 — Comptar línies

Crea un fitxer frases.txt amb 5 frases.

Després:

Llegeix el fitxer
Comptabilitza quantes línies hi ha

Mostra:

El fitxer té 5 línies
## Exercici 5 — Guardar notes d’alumnes

Demana per teclat:

nom alumne
nota

Guarda cada alumne dins d’un fitxer notes.txt amb aquest format:

Anna - 8
Marc - 6
Laura - 9

El programa ha de permetre introduir diversos alumnes.

## Exercici 6 — Llegir i buscar dades

A partir de notes.txt:

Llegeix totes les línies
Mostra només els alumnes amb nota superior o igual a 7
## Exercici 7 — Utilitzar with open

Repeteix l’exercici 6 però utilitzant:

with open(...)

en lloc de open() i close().

🟠 Nivell 3 — Fitxers i directoris
## Exercici 8 — Crear un directori

Fes un programa que:

Mostri el directori actual
Creï un directori anomenat documents
Mostri un missatge si s’ha creat correctament

Utilitza:

os.getcwd()
os.mkdir()
## Exercici 9 — Comprovar si existeix un fitxer

Fes un programa que comprovi si existeix:

dades.txt

Si existeix:

mostra "El fitxer existeix"

Si no existeix:

crea’l automàticament.

Utilitza:

os.path.isfile()
## Exercici 10 — Copiar fitxers

Crea dos directoris:

origen
copia

Posa alguns fitxers dins origen i després:

Copia tots els fitxers a copia

Mostra:

Fitxers copiats correctament

Utilitza:

shutil.copytree()
🔵 Nivell 4 — CSV
## Exercici 11 — Llegir un CSV

Crea un arxiu persones.csv:

nom,edat,ciutat
Anna,20,Barcelona
Marc,22,Girona
Laura,19,Tarragona

Després:

Llegeix el csv

Mostra:

Anna viu a Barcelona
## Exercici 12 — Guardar productes en objectes

Crea una classe:

class Producte

amb:

nom
preu

Llegeix un csv de productes i guarda cada fila dins d’una llista d’objectes.

Finalment mostra tots els productes.

## Exercici 13 — Producte més car

A partir de l’exercici anterior:

Busca quin és el producte més car

Mostra:

El producte més car és Portàtil amb preu 1200
🟣 Nivell 5 — JSON
## Exercici 14 — Llegir JSON

Crea un fitxer usuaris.json:

[
  {"nom":"Anna","edat":20},
  {"nom":"Marc","edat":22}
]

Després:

Llegeix el JSON
Mostra només els noms
## Exercici 15 — Buscar persones majors d’edat

A partir del JSON:

Mostra només les persones amb edat >= 18
Calcula la mitjana d’edat
## Exercici 16 — Afegir dades a un JSON

Demana:

nom
edat

I afegeix el nou usuari al fitxer JSON.

🔴 Nivell 6 — Excel
## Exercici 17 — Crear un Excel

Utilitza xlsxwriter per crear:

despeses.xlsx

amb:

menjar
transport
gimnàs
total automàtic amb fórmula
## Exercici 18 — Llegir un Excel

Utilitza openpyxl per:

Obrir despeses.xlsx
Mostrar totes les cel·les
Mostrar:
número de files
número de columnes
⚫ Nivell 7 — Fusió de fitxers
## Exercici 19 — Emails personalitzats

Crea:

noms.txt
Anna
Marc
Laura
missatge.txt
Tens una reunió demà a les 10h.

El programa ha de generar:

Anna.txt
Marc.txt
Laura.txt

amb contingut:

Hola Anna

Tens una reunió demà a les 10h.
🟤 Nivell 8 — Serialització (pickle)
## Exercici 20 — Guardar objectes

Crea una classe:

class Videojoc

amb:

nom
plataforma
preu

Després:

Crea una llista de videojocs
Guarda-la en un fitxer .dat amb pickle
Carrega les dades
Mostra els videojocs recuperats
🔥 Nivell extra — Exercicis “tipus examen”
## Exercici 21 — Gestor de biblioteca

Crea una classe:

class Llibre

amb:

títol
autor
any

El programa ha de:

Guardar llibres en un CSV
Llegir-los
Mostrar només els llibres posteriors al 2015
## Exercici 22 — Mini agenda JSON

Crea una agenda de contactes amb JSON.

Opcions:

Afegir contacte
Mostrar contactes
Buscar contacte
Eliminar contacte

Les dades han de quedar guardades després de tancar el programa.

## Exercici 23 — Sistema complet de notes

Fes un programa que:

Demani alumnes i notes
Ho guardi en CSV
Calculi:
nota mitjana
nota màxima
alumnes aprovats
Exporti els aprovats a un altre fitxer
🚀 Repte final
## Exercici 24 — Gestor de fitxers complet

Crea una aplicació amb menú:

1. Crear fitxer
2. Escriure fitxer
3. Llegir fitxer
4. Copiar fitxer
5. Eliminar fitxer
6. Crear directori
7. Sortir

Utilitza:

os
shutil
with open
control d’errors amb try/except