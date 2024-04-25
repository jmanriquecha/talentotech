"""Multiplo
Enunciado
Múltiplo: Escriba un programa que pida dos números enteros e imprima si el mayor es múltiplo del menor
Dificultad
Media"""

numero1 = int(input('Por favor ingrese el primer número entero: '))
numero2 = int(input('Por favor ingrese el segundo número entero: '))

"""Funcion para saber si un número es múltiplo de otro

Keyword arguments:
argument -- int mayor, int menor
Return: str
"""
def esMultiplo(mayor, menor):
    multiplo = (mayor % menor) == 0
    
    if multiplo:
        result = f'{mayor} es múltiplo de {menor}'
    else:
        result = f'{mayor} no es múltiplo de {menor}'
    
    return result

# Buscamos cual número es mayor
if(numero1 > numero2):
    print(esMultiplo(numero1, numero2))
else:
    print(esMultiplo(numero2, numero1))