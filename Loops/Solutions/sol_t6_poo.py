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

# ex 33
"""
class Empleado:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Programador(Empleado):
    def __init__(self, nombre, edad, lenguaje):
        Empleado.__init__(self, nombre, edad)
        self.lenguaje = lenguaje

    def mostrar_info(self):
        print(self.nombre, self.edad)

class Diseñador(Empleado):
    def __init__(self, nombre, edad, programa):
        Empleado.__init__(self, nombre, edad)
        self.programa = programa

    def mostrar_info(self):
        print(self.nombre, self.edad)

def main():
    programador = Programador("cata", 20, "java")
    diseñador = Diseñador("didac", 20, "adobe")

    programador.mostrar_info()
    diseñador.mostrar_info()
"""

# ex 34
"""
class Empleado:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        return f"{self.nombre}, {self.edad}"

class Programador(Empleado):
    def __init__(self, nombre, edad, lenguaje):
        Empleado.__init__(self, nombre, edad)
        self.lenguaje = lenguaje
        
    def mostrar_info(self):
        print(f"Programador: {self.nombre} - {self.lenguaje}")

class Diseñador(Empleado):
    def __init__(self, nombre, edad, programa):
        Empleado.__init__(self, nombre, edad)
        self.programa = programa

    def mostrar_info(self):
        print(f"Diseñador: {self.nombre} - {self.programa}")

def main():
    empleados = []

    programador = Programador("cata", 20, "java")
    programador2 = Programador("anabel", 20, "java")
    programador3 = Programador("ivan", 20, "java")
    disenyador = Diseñador("didac", 20, "adobe")
    disenyador2 = Diseñador("pau", 20, "adobe")
    disenyador3 = Diseñador("pol", 20, "adobe")

    empleados.append(programador)
    empleados.append(programador2)
    empleados.append(programador3)
    empleados.append(disenyador)
    empleados.append(disenyador2)
    empleados.append(disenyador3)

    for i, empleado in enumerate(empleados, start=1):
        print(empleado.mostrar_info())
"""

if __name__ == '__main__':
    pass
