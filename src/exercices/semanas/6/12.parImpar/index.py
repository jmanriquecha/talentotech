"""
Par-impar
Enunciado
Par-impar: Solicita al usuario un número entero e imprime si es par o no
Dificultad
Media
"""

#Par-impar

numero = int(input("Ingrese un número entero: "))
es_par = numero % 2 == 0
print(f"El número ingresado es {'par' if es_par else 'impar'}.")