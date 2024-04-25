"""
Contraseña
Enunciado
Contraseña: Cree un programa que solicite una contraseña por teclado e indique si es correcta o no, si es incorrecta, la solicite nuevamente. La contraseña correcta es: "Ilovepython123"
Dificultad
Media
"""

#Contraseña

contrasena_correcta = "Ilovepython123"

while True:
    contrasena_ingresada = input("Ingrese la contraseña: ")
    if contrasena_ingresada == contrasena_correcta:
        print("Contraseña correcta. ¡Bienvenido!")
        break
    else:
        print("Contraseña incorrecta. Inténtelo nuevamente.")
