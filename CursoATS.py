# Entrada de datos

numero = float(input("Introduzca un número: "))

print(f"El número es: {numero}")

# Funciones integradas

a = bin(10)
print (a)
print (int("0b1010", 2))

b = abs(-8)
print(b)

# Redondear un número
c = round(5.6)
print(c)

# Practicar un código

a = float(input("a -> "))
b = float(input("b -> "))
c = float(input("c -> "))

resultado = (a**3 * (b**2 - 2*a*c))/(2*b)
print(f"El resultado es {resultado}")

# Ejercicio

"""Determina la solución lógica de este ejercicio:"""

a = float(input("Introduzca un valor para a ->"))
b = float(input("Introduzca un valor para b ->"))

resultado = print(f"Is {(3+5*8) < 3}" )

# Cap 15 | Intercambiar valores

a = input("a ->")
b = input("b ->")

a , b = b , a

print (f"El nuevo valor de a es: {a}")
print (f"El nuevo valor de a es: {b}")

# Cap 16 | Elementos básicos

import math

r = float(input("Introduzca el valor del radio:"))
area = math.pi * r**2
longitud = 2* math.pi *r

print(f"El area es: {area: .2f}")
print(f"La longitud es: {longitud: .2f}")

# Cap 17 | Elementos básicos 2
"""Descuento de una tienda del 15%, saber el precio de la compra final"""
precio = float(input("Introduzca el precio de la compra: "))

descuento = precio * 0.15
precio_final = precio - descuento
print(f"El precio final del producto es de: ${precio_final: .2f}")

# Cap 18 | Condicionales

numero = int(input("Digite un número: "))
if numero > 0:
    print("El número es positivo")
elif numero == 0:
    print("El número es 0")
else:
    print("El número es negativo")

print("Fin del programa")

# Condicionales combinados

edad = int(input("Digita tu edad:"))
if edad > 0 and edad < 100:
    print("Edad correcta")
    if edad >= 18:
        print("Eres mayor de edad")
else:
        print("No eres mayor de edad")

# Cap 20 | Condicionales

numero1 = float(input("Introduzca el primer número:"))
numero2 = float(input("Introduzca el segundo número:"))

if numero1 % 2 == 0 and numero2 % 2 == 0:
    print("Ambos son pares")
elif numero1 % 2 == 0 and numero2 % 2 != 0:
    print("{numero1} es par")
elif numero1 % 2 != 0 and numero % 2 == 0:
    print("{numero2} es par")
else:
    print("Ambos números son impares")

# Cap 21 | Condicionales

numero1 = int(input("Introduzca el primer número"))
numero2 = int(input("Introduzca el segundo número"))
numero3 = int(input("Introduzca el tercer número"))

if numero1 >= numero2 and numero1 >= numero3:
    print(f"El número mayor es {numero1}") 
elif numero2 >= numero1 and numero2 >= numero3:
    print(f"El número mayor es {numero2}")
elif numero3 >= numero1 and numero3 >= numero2: # o cambiar todo por else:
    print(f"El número mayor es {numero3}")

# Cap 22 | Condicionales

caracter = input("Introduzca un carácter: ").lower() # o podemos crear una linea con: caracter = caracter,lower() (Así mismo existe el upper)

if caracter == 'a' or caracter == 'e' or caracter == 'e' or caracter == 'o' or caracter == 'u':
    print("El caracter es una vocal")
else:
    print("El caracter no es una vocal")

# Cap 23 | Condicionales

num1 = float(input("Introduzca un número: "))
num2 = float(input("Introduzca el segundo dígito:"))

operacion = input("Digite la operación aritmética: ").upper()

if operacion == 'S':
    suma = num1 + num2
    print(f"La suma es {suma}")
elif operacion == 'R':
    resta = num1 - num2
    print(f"La resta es {resta}")
elif operacion == 'P' or operacion == 'M':
    multiplicacion = num1 * num2
    print(f"La multiplicacion es {multiplicacion}")
elif operacion == 'D':
    division = num1 / num2
    print(f"La división es {division}")
else:
    print("Introduzca una operación válida")

# Cap 24 | Condicionales

saldo = 1000

print("Menú")
print("1. Ingresar dinero a la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar saldo disponible")
print("4. Salir")
opcion = int(input("Digite una opción de menú: "))

if opcion == 1:
    suma_monto = float(input("Coloque el monto que desea depositar a la cuenta: "))
    saldo += suma_monto
    print(f"Perfecto!, el nuevo monto es de: {saldo}")
elif opcion == 2:
    retirar_monto = float(input("Coloque la cantidad de saldo que desea retirar: "))
    if retirar_monto > saldo:
        print("No cuenta con el saldo disponible para retirar esa cantidad")
    else:
        saldo -= retirar_monto
    print(f"Perfecto!, el saldo restante que le queda es de {saldo}")
elif opcion == 3:
    print(f"Saldo disponible= ${saldo}")
elif opcion == 4:
    print("Gracias por utilizar su cajero automático")
else:
    print("Error, se equivocó de opción de menú")

# Cap 25 | Colecciones y listas

lista =  ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", 40, 5.55, [1, 2, 3], True]
print(lista[0]) # Lunes
print(lista[2]) # Miercoles
print(lista[-1]) # Viernes, último elemento
print(lista[-4]) # Martes

print(lista[0:2]) #De lunes a miercoles

# End | 29 / 11 / 2024

print(len(lista))

lista = [1, 2, 4, 5]
lista.append(6)
lista.append("Alejandro")

# Agregar un 3 en la lista, pero en el medio
lista.insert(2, 3)
lista.extend([6, 7, 8])
print(lista)
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8]

lista3 = lista1 + lista2
print(lista3)

# Asking questions in the list

lista = [1, 2, 3, 4, 5, "Alejandro"]

print(3 in lista)
print("Alejandro" in lista)
print(lista.index(3))

lista = [1, 2, 3, 4, 5 ,6, "Abraham", 1, 2 ,3 ,4 ,5 ,6, 1]
print(lista.count(1)) # Cuenta los números en la lista
print(lista.find(2)) # Encuentra en que índice está el número pedido
lista.pop(1) # Elimina el número pedido
lista.remove(5) # Elimina los números sin saber la posición

lista = [1, 2, 3, 4, 5, "Alejandro"]*2 # Multiplica la lista por 2
lista = [-1, 0 , -7, 10, 250, -80] 
print(lista.sort()) # Queda ordenada de menos al mayor
print(lista.sort(reverse=True)) # Quedan ordenados de menor

# Cap 27 | Tuplas

tupla = (4, "Hola", 6.78, [1, 2, 3]) 
print(tupla[1:5])
print(4 in tupla) # Devuelve True o False, ocupa la funcion de buscar
print(tupla.count(6.78))

# Transformar de tupla a una lista
lista = list(tupla)
print(lista)

# O viceversa
lista = [4, "Hola", 6.78, [1, 2, 3]]
tupla = tuple(lista)
print(tupla)

# Cap 28 | Conjuntos

conjunto = set()
conjunto = {1, 2, 3, "Hola", 4.56}
conjunto.add(5) # Agrega el caracter en cualquier lado de la lista
conjunto.add("Adios")
conjunto.discard("Hola") # Elimina de la lista
conjunto.clear() #Limpia todo
print(conjunto)

# Buscar números dentro del conjunto

print(3 in conjunto) #True or False
print(3 not in conjunto)

# Cap 29 | Conjuntos

a = {1, 2, 3}
b = {3, 4, 5}

c= a | b # Todos los elementos
d = a & b # Repetición de los 2
e = a - b # Todos menos B, ni la unión
f = a ^ b # Diferencia simétrica, todo menos lo repetido

g = {1, 2, 3, 4, 5} # Esto convierte que a y b sean subconjuntos de g, para que devuelva True tiene que tener todos los elementos
print (a == b) # False
print(a.issubset(g)) #  True

print(a.isdisjoint(b)) # Preguntas si comparten algún elemento entre conjuntos, en este caso a y b comparten el 3, por eso devuelve False

a = frozenset({1, 2, 3}) # Frozenset convierte inmutable, no lo podemos modificar el conjunto, no se puede usar a.add() ni nada

# Cap 30 | Coleeciones, Diccionarios

diccionario = {"azul":"blue", "rojo":"red", "verde":"green"}
diccionario["azul"] = "AZUL"
diccionario["yellow"] = "yellow" # Agregar o actualizar la lista
del(diccionario["verde"])

diccionario = {"Alejandro":[22, 1.73], "José": [22, 1.75], "Martín":[22, 1.77]}
print(diccionario["Alejandro"]) # Todo valor de Alejandro
print(diccionario)

# Cap 31 | Colecciones, diccionarios 2

equipo = {10:"Paulo Dybala", 11:"Tuplas Costa", 7:"Cristiano Ronaldo", 17:"Mario Mandzukic"} #  Tupla, no modificable

print(equipo[10])
print(equipo.get(6, "No existe un jugador con ese dorsal")) # Si no encuentra, lanza la 2da opción
print(10 in equipo)
print(11 in equipo)
print(equipo.keys()) # Muestra solo claves
print(equipo.values()) # Muestra las valores de las claves
print(equipo.items()) # Muestra los 2

equipo.clear() # Eliminar todo el diccionario
print(equipo)

# Cap 32 | Colescciones,  Pilas (Con listas)
"""Pilas es una estructura de dato"""
# Agregando elementos por el final
pila = [1,2,3]

# Agregando elementos por el final
pila.append(4)
pila.append(5)

# Sacar elementos por el final
n = pila.pop()
print(f"Sacando el elemento {n}")
n = pila.pop()
print(f"Sacando el elemento {n}")
n = pila.pop()
print(f"Sacando el elemento {n}")

print(pila)

# Cap 33 | Colas

cola = ["Maria", "Alejandro", "José", "Mario"]

# Agregamos elementos al final de la cola
cola.append("Karla")
cola.append("Flor")
print(cola)

# Sacando elementos por el principio de la cola
n = cola.pop(0)
print(f"La primera en ser atendida será {n}")
n = cola.pop(0)
print(f"La primera en ser atendida será {n}")
n = cola.pop(0)
print(f"La primera en ser atendida será {n}")
n = cola.pop(0)
print(f"La primera en ser atendida será {n}")

print(cola)

# Cap 34 | Colecciones

"""Escriba un programa  donde tenga una lista y que, a continuación, elimine los elementos repetidos, 
por último mostrar la lista"""

lista = [1, 2, 2, 3, 3, 4, 5, 15, "Abraham", 3]

conjunto = set(lista)

lista = list(conjunto)
print(lista)

# Otra forma de 1 línea de código

lista = list(set(lista))
print(lista)

# Cap 35 | Ejercicio 2

"""Escriba un programa que tenga dos listas y que, a continuación, cree las siguientes listas: (En las que no debe haber repeticiones)
- Lista de palabras que aparecen en las dos listas.
- Lista de palabras que aparecen en la primera lista, pero no en la segunda.
- Lista de palabras que aparecen en la segunda lista, pero no en la primera.
- Lista de palabras que aparecen en ambas listas."""

lista1 = {1, 2, 3, 4, 5, 4, 3, 2, 2, 1, 5}
lista2 = {3, 4, 5, 6, 8, 4, 7, 7, 8, 3, 4}

print(f"Los elementos que aparecen en las 2 listas son: {lista1 & lista2}")
print(f"Los elementos que aparecen en la primera lista pero no en la segunda son: {lista1 - lista2}")
print(f"Los elementos que aparecen en la segunda lista pero no en la primera son: {lista1 - lista2}")
print(f"Los elementos que aparecen en la ambas listas son:: {lista1 & lista2}")

# La forma correcta:

lista1 = {1, 2, 3, 4, 5, 4, 3, 2, 2, 1, 5}
lista2 = {3, 4, 5, 6, 8, 4, 7, 7, 8, 3, 4}

# Eliminar los elementos repetidos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

print(f"Los elementos que aparecen en las 2 listas son: {conjunto1 & conjunto2}")
print(f"Los elementos que aparecen en la primera lista pero no en la segunda son: {conjunto1 - conjunto2}")
print(f"Los elementos que aparecen en la segunda lista pero no en la primera son: {conjunto2 - conjunto1}")
print(f"Los elementos que aparecen en la ambas listas son:: {conjunto1 | conjunto2}")

# Cap 36 | Colecciones

"""Escriba un programa donde cree una lista con los siguientes personajes del Señor de los anillos"""

personajes = []
p = {"Nombre":"Aragorn", "Clase":"Guerrero","Raza":"Dúnadan del Norte"}
personajes.append(p) # Agregamos a la lista el personaje

p = {"Nombre": "Gandalf", "Clase":"Mago", "Raza":"Istar"}
personajes.append(p)

p = {"Nombre": "Legolas", "Clase":"Arquero", "Raza":"Elfo"}
personajes.append(p)

print(personajes)

# Cap 37 | Bucles 

import math

# Solicitar un número al usuario
numero = int(input("Digite un número: "))

# Verificar si el número es negativo
while numero < 0:
    print("Error, debería ser un número positivo")
    numero = int(input("Digite un número: "))

# Calcular la raíz cuadrada
print(f"\nSu raíz cuadrada es: {(math.sqrt(numero)):.2f}")

# While como bucle
i = 0

while i < 10:
    print(i)
    i += 1

# Cap 38 | Bucle for, qepd

coleccion = [2, 10, 3, 4, "Alejandro"]

for i in coleccion:
    print(f"Elemento {i}")
    
#Creamos un diccionario
diccionario = {"Alejandro":22, "Maria":23, "José":45, "Luis":12}

# Queremos las edades
for i in diccionario:
    print(f"{diccionario[i]}")

# Queremos los nombres
for i in diccionario:
    print(f"Los nombres de la lista son: {i}")

# Queremos los 2, nombre y edades
for i in diccionario:
    print(f"{i} - Su edad es de: {diccionario[i]}")

for clave,valor in diccionario.items():
    print(f"{clave} - {valor}")

coleccion = "Alejandro"

for i in coleccion:
    print(f"{i}", end="") # El end cambia que el enter se convierta en espacio

# End

