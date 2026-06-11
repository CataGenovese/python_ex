# ex1

"""""
f = open("salutacions.txt", 'w')
f.write("Hola Benvingut al tema de fitxers")
f.close()
"""""

# ex2
"""
f = open("salutacions.txt", 'r')

for i, linia in enumerate(f, start=1):
    print(f"{i}, {linia}")
"""

# Leer archivo
""""
with open("salutacions.txt", 'r') as f:
    contingut = f.read()
    print(contingut)
"""

# ex 3
""""
with open("salutacions.txt", 'a') as f:
    f.write("\nAquesta és una nova línia")

with open("salutacions.txt", 'r') as f:
    contingut = f.read()
    print(contingut)
"""

# ex 3 alternativa
""""
with open("salutacions.txt", 'a+') as f:
    f.write("\nCa")
    f.seek(0)
    contingut = f.read()
    print(contingut)
"""

# ex4
""""
with open("frases.txt", 'w+') as file:
    q_frases = int(input("Quantes frases vols escriure? "))
    for i in range(q_frases):
        inp = input("Introduce una frase: ")
        file.write(inp + "\n")
    file.seek(0)

    contador = 0

    for linea in file:
        contador += 1

    print(f"El fichero tiene {contador} lineas")
"""

# ex5

class Alumne:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

with open("notes.txt", 'w+') as file:
    q_alumnes = int(input("Quantes alumnes vols escriure? "))
    for i in range(q_alumnes):
        nom = input("Introduce el nombre del alumne: ")
        nota =int(input("Introduce la nota del alumne: "))
        alumne = Alumne(nom, nota)
        file.write(f"{alumne.nombre} - {alumne.nota} \n")

""""
    file.seek(0)
    for i in file:
        print(i)
"""
#ex 6
with open("notes.txt", 'r') as file:
    contingut = file.read()
    if alumne.nota > 7:
        print(f"{alumne.nombre} - {alumne.nota}")

