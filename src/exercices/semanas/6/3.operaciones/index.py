"""
Operaciones: Realizar un programa que solicite al usuario dos números e imprimir en pantalla la suma de los números es: La resta de los números es: La multipicacion de los números es
Enunciado
Operaciones: Realizar un programa que solicite al usuario dos números e imprimir en pantalla
la suma de los números es:
La resta de los números es:
La multiplicación de los números es:
"""

num1 = int(input('Ingrese el primer número '))
num2 = int(input('Ingrese el segundo número '))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

print(f'La suma es: {suma}\nLa resta es: {resta}\nLa Multiplicación es: {multiplicacion}')