"""""
with open("saludo.txt", 'w', encoding='utf-8') as file:
    file.write("Hola ")
    file.write("Me llamo Cata")

""""""
count = 0
with open("saludo.txt", 'r', encoding='utf-8') as file:
    for linea in file:
        count +=1
        print(f"lineas: {count}")

""""""
frase = input("Introdueix una frase:")

with open("saludo.txt", 'a', encoding='utf-8') as file:
    file.write(frase)

""""""
with open("saludo.txt", 'r', encoding='utf-8') as file:
    for linea in file:
        if len(linea.strip()) >= 5:
            print(linea.strip())
        else:
            print("NO")

""""""
count = 0

with open("saludo.txt", 'r', encoding='utf-8') as file:
    for line in file:
        cantidad_a = line.count('a')
        if cantidad_a:
            count = count + cantidad_a
    print(count)
    """"""
with open("saludo.txt", 'r', encoding='utf-8') as file:
    textt = file.read()

    with open("text.txt", 'w', encoding='utf-8') as file2:
        file2.write(textt)

"""
with open("saludo.txt", 'r', encoding='utf-8') as file:

    for nom in file:
        nombre= nom.strip()

        with open(nombre + ".txt", 'w', encoding='utf-8') as f2:
            f2.write(f"hola {nombre}")




