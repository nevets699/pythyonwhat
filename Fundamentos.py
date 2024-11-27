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

