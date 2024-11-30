""" EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos."""

# Operadores matemáticos
a = 20
b= 50

# Suma 
suma = a + b
print (suma)

# Resta
resta = b - a 
print (resta)

# Multiplicación
multiplicación = a * b
print (multiplicación)

# División
división = a / b
print (división)

# Exponenciación
exponente = a ** b
print (exponente)

# División entera
c = 10
d = 3

división_entera = c // d
print (división_entera)

""""Ejemplo: 
    Determinar que operadores son divisibles entre 2 o multiplos de ellos, tambien confirmar si son
    mayores o iguales que 5
"""
resultados = [suma, resta, multiplicación, división, exponente, división_entera]

for resultado in resultados:
    if resultado % 2 == 0 and resultado >= 5:
        print (f"{resultado} es divisible entre 2 y mayor igual que 5")
    else: 
        print (f"{resultado} no cumple las condiciones")

# Código int en rango de 10 a 55
""""Crea un programa que imprima por consola todos los números comprendidos 
* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3."""

for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)

# end

""""Como debí haberlo hecho"""

# Operadores aritméticos
print(f"Suma: 10 + 3 = {10+3}")
print(f"Resta: 10 - 3 = {10-3}")
print(f"Multiplicación: 10 * 3 = {10*3}")
print(f"División: 10 / 3 = {10/3}")
print(f"Exponenciación: 10 ** 3 = {10**3}")
print(f"División entera: 10 + 3 = {10//3}")
print(f"Módulo: 10 % 3 = {10%3} (calculas el resto)")

# Operadores de comparación
print(f"Igualdad: 10 == 3 es {10==3}")
print(f"Desigualdad: 10 != 3 es {10 != 3}")
print(f"Mayor que: 10 > 3 es {10 > 3}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 >= 3 es {10 >= 10}")
print(f"Menor o igual que: 10 <= 3 es {10 <= 3}")

# Operadores lógicos
print(f"And &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"Or ||: 10 + 3 == 13 or 5 - 1 == 6 es {10 + 3 == 13 or 5 - 1 == 6}")
print(f"Not !!: 10 + 3 == 14 es {not 10 + 3 == 14} (Devuelve True lo falso")

"""Prioridad de estos:
1. Not
2. And
3. Or
"""

# Operadores de asignación
my_number = 11 #asignado
print(my_number)
my_number += 1 # suma y asignación
print(my_number)
my_number -= 1 # resta y asignación
print(my_number)
my_number *= 1 # multiplicación y asignación
print(my_number)
my_number /= 1 # división y asignación
print(my_number)
my_number %= 1 # módulo y asignación
print(my_number)
my_number **= 1 # exponenciación y asignación
print(my_number)
my_number //= 1 # división_entera y asignación
print(my_number)

# Operadores de identidad
my_newnumber = my_number
print(f"my_number is my_newnumber es {my_number is my_newnumber}")
print(f"my_number is not my_newnumber es {my_number is not my_newnumber}")

# Operadores de pertenencia
print(f"'u' in 'moure'")

