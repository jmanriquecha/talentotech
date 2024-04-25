"""Multiplicacion
Enunciado
Multiplicación: Hacer un programa que solicite al usuario números enteros siempre y cuando sean menores de 10 e imprima la multiplicación de cada uno de los números digitados(3*5*6*3..). Cuando el usuario digite un número mayor de 10 imprima la multiplicación que lleva hasta el momento
Dificultad
Media

Instrucciones"""

total = 0

while True:
    num = int(input('"CALCULADORA:" Ingrese un valor entero menor a 10: '))
    if(num > 10):
        print(total)
        break
    else:
        if(total == 0):
            total = 1
            
        total *= num
        