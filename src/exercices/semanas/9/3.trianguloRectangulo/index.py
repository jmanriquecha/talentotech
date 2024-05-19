""" 
Triangulo Rectangulo
Enunciado
Triangulo Rectangulo: Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido. Ejm para n=9 1 3 1 5 3 1 7 5 3 1 9 7 5 3 1
Dificultad
Media

Instrucciones
"""

#Triangulo Rectangulo

altura = int(input("Ingrese un número entero para la altura del triángulo: "))

for i in range(1, altura + 1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print()