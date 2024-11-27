# Longitud de un mensaje

message = "Hello World"
print(len(message))

# Escribir solo un carácter de una oración

print(message[0])
print(message[5])

# Escribir a partir de cierta letra

print(message[0:5])
print(message[6:])

# Contar () tiene la oración

print(message.count("Hello"))
print(message.count("o"))

# Encontrar código en la oración

print(message.find("o"))
print(message.find("World"))

""""Ahora supongamos que queremos reemplazar un mensaje, en tal caso:"""

mensaje = "Hola Mundo"
nuevo_mensaje = message.replace('World', 'Universe')

print(nuevo_mensaje)

"Sumar variables"

mensaje1 = 'Hola'
mensaje2 = 'Fran'

suma_mensajes = mensaje1 + ', ' + mensaje2 + '. Welcome!'
print (suma_mensajes)

"""No es recomendable usar muchos + (suma) para un código debido al espacio que va a utilizar, podemos optar por otras opciones"""

suma_mensajes2 = "{}, {}. Welcome!".format(mensaje1, mensaje2)
print(suma_mensajes2)

suma_mensajes3 = "{}, {}, {}. Acabó la linea de código".format(mensaje, mensaje1, mensaje2)
print(suma_mensajes3)

# Sacando el método formant y reemplazando directamente las funciones dentro de las cadenas

suma_mensajes5 = f"{mensaje1.lower()}, {mensaje2.upper()}. Welcome!"
print(suma_mensajes5)

"""Dir nos lista todos los atributos y métodos que tenemos para usar"""

print(dir(mensaje))

"""Help str"""

print(help(str.lower))