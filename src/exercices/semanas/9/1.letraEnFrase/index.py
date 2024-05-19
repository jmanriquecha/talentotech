"""
Letra en frase
Enunciado
Letra en frase: Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
Dificultad
Media

Instrucciones
"""

frase = input('Por favor ingrese una frase: ')
letra = input('Por favor ingrese una letra a buscar dentro de la frase: ')

seRepite = frase.count(letra)

print(seRepite)