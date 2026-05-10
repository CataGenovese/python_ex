# ex 23
"""""
def suma(n1, n2):
    return n1 + n2

def main():
    n1 =int(input("N1: "))
    n2 =int(input("N2: "))

    print(suma(n1, n2))
"""""

import random
# ex 24
"""""
def r():
    for i in range(10):
        return random.random()

def main():
    print(r())
"""""

# ex 25
"""""
def suma(list):
    total= 0
    for i, sum in enumerate(list):
        total += sum
    return total

def main():
    list1 = [2, 2, 2, 2]
    print(suma(list1))
"""""

# ex 26
"""""
def suma(list):
    max= 0
    for i, sum in enumerate(list):
        if sum > max:
            max = sum
    return max

def main():
    list1 = [2, 2, 20, 18]
    print(suma(list1))
"""""

# ex 27
"""""
def eliminar_vocal(frase):
    list_frase_no_vocals = []
    for i in frase:
        if i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
            list_frase_no_vocals.append(i)
    print(list_frase_no_vocals)

# ALTERNATIVA
def not_vocal(frase):
    list= []
    for i in frase:
        if i not in "aeiou":
            list.append(i)
    return "".join(list)
"""""

if __name__ == "__main__":
    pass