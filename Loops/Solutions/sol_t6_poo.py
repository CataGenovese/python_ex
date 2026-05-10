# ex 29
"""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(self.nombre, self.edad)

def main():
    nombre = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    persona = Persona(nombre, edad)
    persona.mostrar_info()
"""
# ex31
"""
class Coche:
    def __init__(self, matricula, color, puertas):
        self.matricula = matricula
        self.color = color
        self.puertas = puertas

def main():
    coches= []
    coche1 = Coche("aaa", "red", 4)
    coche2 = Coche("bbb", "blue", 4)
    coche3 = Coche("ccc", "yellow", 4)

    coches.append(coche1)
    coches.append(coche2)
    coches.append(coche3)

    for i, coche in enumerate(coches, start=1):
        print(f"Coche {i}: {coche.matricula}, {coche.color}, {coche.puertas}")
"""

# ex 32
"""
class Factura:
    def __init__(self):
        self.lista = []

    def calcular_factura(self):
        total = 0
        for i, factura in enumerate(self.lista):
            total += factura.precio * factura.cantidad

        return total


class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad


def main():
    p1 = Producto("bloc", 12, 2 )
    p2= Producto("boli", 3, 1 )
    p3 = Producto("lapiz", 2, 2 )

    factura = Factura()
    factura.lista.append(p1)
    factura.lista.append(p2)
    factura.lista.append(p3)

    print(factura.calcular_factura())
"""

class Empleado:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Programador(Empleado):


if __name__ == '__main__':
    main()