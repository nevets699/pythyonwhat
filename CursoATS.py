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
