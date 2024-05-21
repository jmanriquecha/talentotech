""" 
Adivinanza
Enunciado
Adivinanza: Crea un programa que genere un número aleatorio entre 1 y 10 y permita al usuario intentar adivinarlo. El programa debe dar pistas indicando si el número ingresado es mayor o menor al número secreto. El juego debe continuar hasta que el usuario adivine el número.
Dificultad
Media

Instrucciones
"""
import random

aleatorio = random.randint(1, 10)
while True:
    user = int(input('Ingresa un número entre 1 y 10 para adivinar: '))
    if user == aleatorio:
        print(f'Genial adivinaste el número es {user}')
        break
    else:
        if user > aleatorio:
            print('Estuviste cerca, Pista: Ingresaste un número mayor')
        else:
            print('Vas por buen camino, intenta ingresar un número mayor esta vez')