"""
Inversion
Enunciado
Inversión: Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
Dificultad
Media
"""

#Inversion

cantidad_invertir = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interés anual (%): "))
num_anios = int(input("Ingrese el número de años: "))

for anio in range(1, num_anios + 1):
    cantidad_invertir *= 1 + (interes_anual / 100)
    print(f"Año {anio}: Capital acumulado = {round(cantidad_invertir, 2)}")