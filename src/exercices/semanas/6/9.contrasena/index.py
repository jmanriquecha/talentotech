""" 
Verificacion contraseña
Enunciado
Verificación contraseña: Solicita al usuario que ingrese una contraseña, verifica si la contraseña tiene al menos 8 caracteres y un número e imprime :Contraseña valida o invalida según sea el caso
Dificultad
Media
"""

password = input('Su contraseña debe tener por lo menos 8 caracteres y contener un número ')

#Validacion contraseña
es_valida = len(password) >= 8 and any(char.isdigit() for char in password)
print(f"¿La contraseña es válida? {es_valida}")