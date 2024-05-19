""" 
Materias
Enunciado
Materias: Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia, Lenguaje y Programación) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En has sacado dónde es cada una de las asignaturas de la lista y cada una de las correspondientes notas introducidas por el usuario.
Dificultad
Química

Instrucciones

"""


asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lenguaje", "Programacion"]
notas = []

for asignatura in asignaturas:
    nota = float(input(f"Ingrese la nota de {asignatura}: "))
    notas.append(nota)

print("\nResumen de notas:")
for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}")