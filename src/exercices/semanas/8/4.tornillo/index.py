"""Tornillo
Enunciado
Tornillo: Cree un programa que solicite el tamaño de un tornillo e imprima su tamaño de acuerdo a las sigueintes condiciones:De 1 cm(incluido) hasta 3 cm(no incluido) es pequeño De 3 cm(incluido) hasta 5 cm(no incluido) es mediano De 5 cm(incluido) hasta 6.5 cm(no incluido) es grande de 6.5cm (incluido) hasta 8.5 cm(no incluido) es muy grande De 8.5 cm(incluido) en adelante es gigante
Dificultad
Media

Instrucciones"""

tamanoTornillo = float(input('Ingrese el tamaño del tornillo: '))

if (tamanoTornillo >= 1) & (tamanoTornillo < 3):
    result = 'Pequeño'
elif (tamanoTornillo >= 3) & (tamanoTornillo < 5):
    result = 'Mediano'
elif (tamanoTornillo >= 5) & (tamanoTornillo < 6.5):
    result = 'Grande'
elif (tamanoTornillo >= 6.5) & (tamanoTornillo < 8.5):
    result = 'Muy grande'
else:
    result = 'Gigante'

print(f'El tornillo es {result}')

lista = [1,2,3,4,5]
for elemento in lista:
    print(elemento)