import math

"""Factorial
Enunciado
Factorial: Realizar un programa que calcule el factorial de un número que ingrese un usuario, el número debe ser > 0 y < 20, de no ser así, debe pedir el número tantas veces como sea necesario hasta que cumpla la condición. Recuerda usar la librería math
Dificultad
Media

Instrucciones"""


while True:
    numero = int(input('Ingrese un número (> 0 y < 20) para calcular el factorial: '))
    if (numero > 0) & (numero < 20):
        print(f'El factorial de {numero} es: {math.factorial(numero)}')
        break
    else: 
        print('Estas fuera de rango, por favor vuelva a intentar: ') 