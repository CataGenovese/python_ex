# EX 1
frutas = ["poma", "platan", "maduixa"]

for i, fruta in enumerate(frutas):
    pass
    # print(i, fruta)

# EX 2
notes = [4, 7, 9, 2]
for i, nota in enumerate(notes, start=1):
    pass
   # print(f"Alumne  {i} :  {nota}")

# EX 3
notes = [4, 7, 9, 2]
for i, nota in enumerate(notes):
    if nota > 5:
        pass
       # print(f"Alumne {i}: aprovat amb un {nota}")

# EX 4
class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.preu = preu

llista_productes = []

producte1= Producte("Cola", 2)
producte2= Producte("Pizza", 8)
producte3= Producte("Aigua", 1)

llista_productes.append(producte1)
llista_productes.append(producte2)
llista_productes.append(producte3)

for i, llista in enumerate(llista_productes, start=1):
    pass
    # print(f"{i} - {llista.nom} : {llista.preu}euros")

# EX 5
class Jugador:
    def __init__(self, nom, punts):
        self.nom = nom
        self.punts = punts

llista_jugadors = []

jugador1 = Jugador("Marc", 23)
jugador2 = Jugador("Anna ", 12)
jugador3 = Jugador("Pol ", 30)

llista_jugadors.append(jugador1)
llista_jugadors.append(jugador2)
llista_jugadors.append(jugador3)

for i, jugador in enumerate(llista_jugadors, start=1):
    pass
    # print(f"Jugador {i} : {jugador.nom} - {jugador.punts} punts")


# EX 6
""""
class Biblioteca:
    def __init__(self, nom):
        self.nom = nom
        self.llista_llibres= []

class Llibre:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

bibliotecas = []
q_bibliotecas = int(input("Quantitat bibliotecas: "))

for j in range(q_bibliotecas):
    nom_bibliotecas = input("Nom bibliotecas: ")
    biblioteca = Biblioteca(nom_bibliotecas)
    bibliotecas.append(biblioteca)
    q_llibres = int(input("Quantitat llibres: "))

    for i in range(q_llibres):
        nom_llibre = input("Nom llibre: ")
        autor = input("Nom autor: ")
        libro = Llibre(nom_llibre, autor)
        biblioteca.llista_llibres.append(libro)


for i, biblio in enumerate(bibliotecas, start=1):
    print(f"Biblioteca {i} : {biblio.nom}")

    for j, llibre in enumerate(biblio.llista_llibres, start=1):
        print(f"Llibre {j} : {llibre.titulo}")

"""
# EX 7

class Comanda:
    def __init__(self):
        self.llista_productes = []

    def calcul_preu(self):
        total = 0
        for producto in self.llista_productes:
            total += producto.preu * producto.cantidad
        return total

class Producte:
    def __init__(self, nom, cantidad, preu):
        self.nom = nom
        self.cantidad = cantidad
        self.preu = preu

comandas= []
q_comandas = int(input("Quantitat comandas: "))

for j in range(q_comandas):
    comanda = Comanda()
    q_productes = int(input("Quantitat productes: "))

    for i in range(q_productes):
        nom = input("Nom: ")
        cantidad = int(input("Cantidad: "))
        preu = int(input("Preu: "))
        producte = Producte(nom, cantidad, preu)
        comanda.llista_productes.append(producte)
    comandas.append(comanda)

for i, comanda in enumerate(comandas, start=1):
    print(f"Comanda {i}")

    for j, producte in enumerate(comanda.llista_productes, start=1):
        print(f"Producte {j} : {producte.nom}")
    print(f"TOTAL: {comanda.calcul_preu()}")

