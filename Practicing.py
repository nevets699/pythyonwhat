# Solicitar valores para A y B
a = int(input("Introduzca un valor para a ->"))
b = int(input("Introduzca un valor para b ->"))

# Operaciones lógicas
operacion1 = (3+5*8) < 3
operacion2 = ((-6/3*4) + 2 < 2)
operacion3 = a > b

# Calcular resultado
resultado = operacion1 and operacion2 or operacion3

# Imprimir resultado
print(f"El resultado es: {resultado}")

# Otra manera de escribir el mismo código

a = float(input("a ->"))
b = float(input("b ->"))

resultado = ((3+5*8)<3 and (-6/3*4)+2<2) or (a>b)

print(f"El resultado es: {resultado}")