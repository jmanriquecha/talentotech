"""Tipo de Triangulo
Enunciado
Tipo de Triangulo: Cree un programa que solicite la longitud de los 3 lados de un triángulo e imprima si es equilátero(3 lados iguales), isósceles(2 lados iguales) o escaleno(todos los lados diferentes)
Dificultad
Media"""

input('Programa para saber el tipo de un triángulo')
lado1 = float(input('Ingrese el tamaño del lado 1: '))
lado2 = float(input('Ingrese el tamaño del lado 2: '))
lado3 = float(input('Ingrese el tamaño del lado 3: '))

equilatero = (lado1 == lado2) & (lado1 == lado3)
isoscele = (lado1 == lado2) | (lado1 == lado3) | (lado2 == lado3)
escaleno = (lado1 != lado2) | (lado1 != lado3) | (lado2 != lado3)

if equilatero:
    tipo = 'Equilátero'
elif isoscele:
    tipo = 'Iscóceles'
else:
    tipo = 'Escaleno'
    
print(f'El Triángulo es {tipo}')
