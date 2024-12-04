"""Desafío: Sistema de Gestión de Estudiantes
Descripción:
Vas a crear un pequeño sistema de gestión de estudiantes para una escuela. Este sistema debe permitir al usuario realizar las siguientes acciones:

Agregar un nuevo estudiante: El usuario ingresa el nombre, la edad y las calificaciones en diferentes materias.

Mostrar información de un estudiante: El usuario ingresa el nombre del estudiante y el sistema muestra su edad y promedio de calificaciones.

Eliminar un estudiante: El usuario ingresa el nombre del estudiante y lo elimina del sistema.

Mostrar todos los estudiantes: El sistema muestra la lista de todos los estudiantes registrados.

Salir: Termina el programa.

Requisitos:
Utiliza un diccionario para almacenar la información de los estudiantes. La clave será el nombre del estudiante y el valor será otro diccionario que contenga la edad y las calificaciones.

Permite la entrada del usuario para seleccionar qué acción desea realizar.

Utiliza bucles y condicionales para implementar la lógica del menú."""

# Sistema de estudiantes
print("¡Bienvenido al sistema de estudiantes!")
print("1. Agregar un nuevo estudiante.")
print("2. Mostrar información de un estudiante.")
print("3. Mostrar todos los estudiantes.")
print("4. Salir")
opcion = print(int(input("Seleccione la opción que desee realizar: ")))

# Estudiantes
estudiante1 = {"Nombre":"Alejandro", "Edad:":"22", "Calificaciones":"17"}
estudiante2 = {"Nombre":"Abraham", "Edad:":"17", "Calificaciones":"16"}
estudiante3 = {"Nombre":"Esteban", "Edad:":"18", "Calificaciones":"20"}
estudiante4 = {"Nombre":"Franco", "Edad:":"17", "Calificaciones":"15"}

numero_estudiantes = estudiante1 + estudiante2 + estudiante3 + estudiante4
# Opción 1
if opcion == 1:
    nombre = input("Nombre del estudiante: ")
    edad = input("Edad del estudiante: ")
    calificacion = input("Introduzca la calificación del estudiante: ")

# 4/12/2024



