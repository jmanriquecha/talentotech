""" 
Validacion rango
Enunciado
Validación rango: Solicita al usuario un número y comprueba si el número está en el rango de 10 a 20(inclusive) e imprime el resultado
Dificultad
Media
"""

#Validacion rango
numero = int(input("Ingrese un número: "))
en_rango = 10 <= numero <= 20
print(f"¿El número está en el rango de 10 a 20? {en_rango}")