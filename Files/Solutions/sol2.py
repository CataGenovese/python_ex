"""with open("datos.txt", "w", encoding="utf-8") as f:
    f.write("Hola\n")
    f.write("Adios")
"""
"""""
with open("saludo.txt", "w") as file:
    file.write("Hola\n")
    file.write("Me llamo cata")
"""

"""""
with open("saludo.txt", "r") as file:
    contador = 0
    for f in file:
        contador += 1

    print(contador)
"""""
"""""
frase = input("Inserta una frase para el fichero")
with open("frases.txt", "a") as file:
    file.write(frase + "\n")

with open("frases.txt", "r") as f:
    for i in f:
        print(i.strip())
"""""

# ------------ NIVEL 2
"""""
with open("frases.txt", "r") as file:
    for line in file:
        if len(line.strip()) > 8:
            print(line.strip())
        else:
            print("no mas largo que 5")
"""""

"""""
with open("frases.txt", "r") as file:
    contador_a =0
    for line in file:
        contador_a = contador_a + line.count("a")
    print(contador_a)
"""""
#ex7
"""""
with open("frases.txt", "r") as file:
    read = file.read()

with open("copiafrase.txt", "w") as f:
    f.write(read)
"""""
"""""
with open("saludo.txt", "w") as file:
    contador = 0

    while contador < 3:
        noms = input("Inserta nombre: ")
        file.write(noms + "\n")
        contador += 1
"""""
with open("../S2/saludo.txt", "r") as file:
    for nom in file:
        nombre = nom.strip()
        
        with open(nombre + ".txt", "w") as new:
            new.write("Hola " + nombre)


"""""
buscar_dni = input("DNI: ")
trobat = False

with open("datos.txt", "r") as file:
    for linea in file:
        datos = linea.split()

        dni= datos[0]
        age= datos[1]

        if dni == buscar_dni:
            print("Edad", age)
            trobat= True

if not trobat:
    print("No encontrado")
"""""




