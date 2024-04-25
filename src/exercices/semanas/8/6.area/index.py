"""Area
Enunciado
Área: Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo (T o t) o la de un círculo (C o c). Si contesta que quiere calcular el área de un triángulo solicite base y altura, de lo contrario solicite el radio e imprima el área correspondiente
Dificultad
Media

Instrucciones"""

usuario = input('Si quiere calcular el área de un triángulo (T ó t) o la de un círculo (C ó c)')

# Área de un triángulo
def areaTriangulo(base, altura):
    return round((altura * base) / 2, 2)

# Área de un círculo
def areaCirculo(radio):
    PI = 3.1416
    return round(PI * (radio ** 2), 2) 

if usuario.lower() == 't':
    base = float(input('Por favor ingrese la base del triángulo: '))
    altura = float(input('Por favor ingrese la altura del triángulo: '))
    print(f'El área del triángulo es de: {areaTriangulo(base, altura)} cm^2')
elif usuario.lower() == 'c':
    radio = float(input('Por favor ingrese el radio del círculo: '))
    print(f'El área del círculo es de: {areaCirculo(radio)} cm^2')
else:
    print('No ha seleccionado una opción valida: ')