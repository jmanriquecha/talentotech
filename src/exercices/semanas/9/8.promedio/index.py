""" 
Promedio
Enunciado
Promedio: Escribe un programa que solicite al usuario ingresar notas de estudiantes. El programa debe permitir al usuario ingresar cuantas notas desee. Cuando el usuario ingrese -1, el programa debe calcular y mostrar el promedio de las notas ingresadas.
Dificultad
Media

Instrucciones
Física
"""

cont = 1
acumulado = 0
print('PROGRAMA PARA CALCULAR PROMEDIO DE NOTAS: ')
print('Escriba (-1) para terminar y calcular el promedio\n')
while True:
    notas = float(input(f'Ingrese la nota número {cont}: '))
    if(not notas == -1):
        acumulado += notas
        cont += 1
    else:
        print(f'Promedio de las notas es: {acumulado/(cont-1)}')
        break  