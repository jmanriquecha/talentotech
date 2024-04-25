"""Tablas de multiplicar
Enunciado
Tablas de multiplicar: Realizar un programa que solicite un número que sea menor a 10(valida que si sea menor a 10) y luego solicite desde que número hasta que número desea ver la tabla de multiplicar por ejm la tabla del 2 desde el 7 hasta el 20, el sistema imprimirá 2*7= ...2*20=...
Dificultad
Media

Instrucciones"""

num1 = int(input('Ingrese un número menor que díez: '))

if(num1 < 10):
    numInical = int(input(f'Desde que número quiere visualizar la tabla del {num1} '))
    numFinal = int(input(f'Hasta que número desea visualizar la tabla del {num1} '))
    
    for n in range(numInical, numFinal + 1):
        print(f'{num1} X {n} = {num1 * n}')
else:
    print('Fuera de rango')