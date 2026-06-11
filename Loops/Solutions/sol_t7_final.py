#ex 35
"""
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_libros = []

    def mostrar_info(self):
        return f"Nombre: {self.nombre} "

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


def main():
    libro1 = Libro("HP", "JKR")
    libro2 = Libro("Percy Jackson", "Cata")
    libro3 = Libro("Persepolis", "Mk")
    libro4 = Libro("Metamorfosis", "Kafka")

    bibliotecas = []

    q_bibliotecas = int(input("Cantida de bibliotecas: "))
    for i in range(q_bibliotecas):
        nom_biblioteca = input("Nombre biblioteca: ")

        biblioteca = Biblioteca(nom_biblioteca)

        biblioteca.lista_libros.append(libro1)
        biblioteca.lista_libros.append(libro2)
        biblioteca.lista_libros.append(libro3)
        biblioteca.lista_libros.append(libro4)

        bibliotecas.append(biblioteca)

    for i, biblio in enumerate(bibliotecas, start=1):
        print(f"\nBiblioteca {i}: {biblio.nombre}")

        for j, libro in enumerate(biblio.lista_libros, start=1):
            print(f"libro n {j}: {libro.titulo} ")
"""
class Pedidos:
    def __init__(self, n_pedido):
        self.n_pedido = n_pedido
        self.lista_productos = []

        


if __name__ == "__main__":
    main()