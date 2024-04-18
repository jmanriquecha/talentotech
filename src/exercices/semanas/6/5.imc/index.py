""" 
IMC
Enunciado
IMC: Escribir un programa que pida al usuario su peso(en kg) y estatura (en metros), calcule el índice de masa corporal(IMC) y muestre en pantalla la frase: Tu índice de masa corporal es: , donde imc es el cálculo realizado. Este imc debe estar redondeado con dos decimales
"""

peso = float(input('Ingrese su peso en Kg '))
estatura = float(input('Ingrese su estatura en metros '))

imc = peso / (estatura ** 2)

print(f'Tu índice de masa corporal es: {imc}')