# 🟢 TEMA 1 — BUCLES BÁSICOS (range, for)

## 🔹 Nivel 1 — range() básico

**Ejercicio 1**
Imprime los números del 0 al 9.

**Ejercicio 2**
Imprime los números del 5 al 15.

**Ejercicio 3**
Imprime los números del 10 al 0 (descendente).

**Ejercicio 4**
Imprime los múltiplos de 3 del 0 al 30.

## 🔹 Nivel 2 — range() con lógica

**Ejercicio 5**
Imprime solo los números pares del 0 al 20.

**Ejercicio 6**
Imprime los números del 1 al 50, pero solo los que acaben en 5.

**Ejercicio 7**
Suma todos los números del 1 al 100.

## 🔹 Nivel 3 — patrones con bucles

**Ejercicio 8**
Imprime:
```text
*
**
***
****
*****
```

**Ejercicio 9**
Imprime los números así:
```text
1
12
123
1234
```

---

# 🟡 TEMA 2 — LISTAS + ÍNDICES

## 🔹 Nivel 1 — acceder con índice

**Ejercicio 10**
Dada:
```python
frutas = ["manzana", "pera", "uva", "plátano"]
```
Imprime:
```text
0 manzana
1 pera
2 uva
3 plátano
```

## 🔹 Nivel 2 — recorrer listas

**Ejercicio 11**
Dada:
```python
colores = ["rojo", "azul", "verde", "negro"]
```
Imprime todos los colores.

**Ejercicio 12**
Imprime solo los elementos en posición impar de la lista anterior.

## 🔹 Nivel 3 — lógica con listas

**Ejercicio 13**
Suma todos los números de:
```python
nums = [3, 5, 2, 8, 10]
```
**Ejercicio 13.2**
Dissenyar una funció que, donada una frase, la mostri per pantalla envoltada d’asteriscos.
```python
********
* hola *
********
```

**Ejercicio 14**
Encuentra el número más grande sin usar la función `max()`.

---

# 🟠 TEMA 3 — enumerate()

## 🔹 Nivel 1 — básico

**Ejercicio 15**
Dada:
```python
frutas = ["poma", "platan", "maduixa"]
```
Muestra:
```text
0 - poma
1 - platan
2 - maduixa
```

## 🔹 Nivel 2 — enumerate clásico de clase

**Ejercicio 16**
Dada:
```python
notes = [4, 7, 9, 2]
```
Muestra:
```text
Alumne 1: 4
Alumne 2: 7
Alumne 3: 9
Alumne 4: 2
```

## 🔹 Nivel 3 — condiciones con enumerate

**Ejercicio 17**
Muestra solo aprobados (>5):
```python
notes = [4, 7, 9, 2, 6]
```

## 🔹 Nivel 4 — errores típicos de examen

**Ejercicio 18**
Muestra solo los números pares con su índice.

---

# 🔴 TEMA 4 — STRINGS + BUCLES

## 🔹 Nivel 1
**Ejercicio 19**
Pide una palabra y muestra cada letra con su índice.

## 🔹 Nivel 2
**Ejercicio 20**
Cuenta cuántas vocales tiene una palabra.

## 🔹 Nivel 3
**Ejercicio 21**
Invierte una palabra SIN usar `[::-1]`.

## 🔹 Nivel 4
**Ejercicio 22**
Comprueba si una palabra es palíndromo.

---

# 🟣 TEMA 5 — FUNCIONES (MODULARIDAD)

## 🔹 Nivel 1 — funciones simples

**Ejercicio 23**
Crea una función que sume dos números.

**Ejercicio 24**
Crea una función que devuelva un número aleatorio del 1 al 10.

## 🔹 Nivel 2 — funciones con listas

**Ejercicio 25**
Crea una función que reciba una lista y devuelva la suma.

**Ejercicio 26**
Crea una función que reciba una lista y devuelva el máximo.

## 🔹 Nivel 3 — diseño modular

**Ejercicio 27**
Haz una función que elimine las vocales de una frase.

---

# 🔵 TEMA 6 — POO (CLASES Y OBJETOS)

## 🔹 Nivel 1 — clases básicas

**Ejercicio 29**
Crea la clase `Persona`:
* Atributos: `nombre`, `edad`
* Método: mostrar información.

## 🔹 Nivel 2 — constructor

**Ejercicio 30**
Crea la clase `Coche` con constructor (`__init__`):
* Atributos: `matrícula`, `color`, `puertas`

## 🔹 Nivel 3 — lista de objetos

**Ejercicio 31**
Crea 3 coches y guárdalos en una lista. Recorre la lista y muestra todos los coches.

## 🔹 Nivel 4 — composición (muy importante)

**Ejercicio 32**
Crea una clase `Factura`:
* Atributos: lista de productos.
* Cada producto tiene: `nombre`, `precio`, `cantidad`.
* Método: Calcula el total de la factura.

## 🔹 Nivel 5 — herencia

**Ejercicio 33**
Crea una clase base `Empleado`.
Crea clases hijas: `Programador`, `Diseñador`.
* Cada uno debe tener un método `mostrarInfo()` diferente.

## 🔹 Nivel 6 — polimorfismo

**Ejercicio 34**
Crea una lista de empleados distintos (mezclando programadores y diseñadores).
Recorre la lista y muestra a todos invocando el mismo método `mostrarInfo()`.

---

# TEMA 7 — EXAMEN MIXTO (TIPO FINAL)

**Ejercicio 35**
Sistema de biblioteca:
* Clase `Biblioteca`.
* Lista de libros.
* Cada libro tiene `título` y `autor`.
* Mostrar todas las bibliotecas con sus libros usando `enumerate`.

**Ejercicio 36**
Sistema de pedidos:
* Clase `Pedido`.
* Lista de productos.
* Calcular total.
* Mostrar factura tipo ticket.

**Ejercicio 37**
Sistema de estudiantes:
* Clase `Estudiante`.
* Atributos: `nombre`, `notas`.
* Mostrar aprobados con índice usando `enumerate`.