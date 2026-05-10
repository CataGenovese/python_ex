# ex19
"""""
palabra = input("Palabra: ")
for i, letra in enumerate(palabra):
    print(f"{i}, {letra} ")
"""""

# ex 19.2
""""
frase = input("Palabra: ")
palabra = frase.split()

for i, palabra in enumerate(palabra):
    print(f"{i}, {palabra} ")
"""
#ex 20
"""
palabra = input("Palabra: ")
contador = 0
for i in palabra:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        contador += 1
print(contador)
"""

#ex 21
"""""
palabra = input("Palabra: ")
invertida = ""

for letra in palabra:
    invertida = letra + invertida

print(invertida)
"""""

# ex 22
inp = input("Palabra: ")
invertida = ""
for letra in inp:
    invertida = letra + invertida

if invertida == inp:
    print("Palindromo")
else:
    print("No palindromo")


