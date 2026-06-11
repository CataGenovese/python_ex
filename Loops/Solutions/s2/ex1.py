
import random
"""""
frutas = ["manzana", "pera", "uva", "plátano"]

for i, fruta in enumerate(frutas):
    print(f"{i}:  {fruta}")
"""

# ex 16
"""
notas = [4,7,9,2]

for i, nota in enumerate(notas[1:], start=1):
    print(f"Alumne{i}: {nota}")
"""
"""
class Persona:
    def __init__(self, nom, edad, ciudad):
        self.nom = nom
        self.edad = edad
        self.ciudad = ciudad

class Animal:
    nombre = " .  "
    edad = 0
    especie = " . "

a1 = Animal()
a1.nombre = "Rex"
# print(a1.nombre, a1.edad, a1.especie)

p1 = Persona("cata", 12, "bcn")

p2 = Persona("cata", 12, "bcn")
print(p1 == p2)

print(p1.nom, p1.edad, p1.ciudad)
p1.nom = "dídac"
print(p1.nom, p1.edad, p1.ciudad)

class Persona:
    def__init__(self, nombre, color_ojos, peso):
    self.nombre = nombre
    self.color_ojos = color_ojos
    self.peso = peso
   """

"""""
def obtenir_vocal_aleatoria():
    vocals = ["a", "e", "i", "o", "u"]
    return random.choice(vocals).upper()

def main():
    print(obtenir_vocal_aleatoria())

main()
"""
def borrar_vocals(frase):


def main():
    frase = input("Inserte frase: ")

    print(borrar_vocals(frase))

main()




