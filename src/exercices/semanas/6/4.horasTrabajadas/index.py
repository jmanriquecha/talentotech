""" 
Horas trabajadas
Enunciado
Horas trabajadas: Escribir un programa que pregunte al usuario por el número de horas trabajadas y el costo por hora. Después muestre en pantalla el pago que le corresponde
"""

horas = float(input('Por favor ingrese el número de horas trabajadas '))
valorHora = float(input('Por favor ingrese el valor de cada hora '))

pago = horas * valorHora

print(f'Le corresponde el siguiente pago: {pago}')