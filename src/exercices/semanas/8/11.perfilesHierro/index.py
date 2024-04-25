"""Perfiles de hierro
Enunciado
Perfiles de hierro: Una planta que fabrica perfiles de hierro posee un lote de n piezas.
Diseñar un programa que pida ingresar por teclado la cantidad de piezas a procesar e ingrese la longitud de cada perfil, sabiendo que la pieza cuya longitud este comprendida entre 1.20 y 1.30 son aptas. Imprimir la cantidad de piezas del lote que son aptas
Dificultad
Media

Instrucciones"""

cantidad =  int(input('Ingrese la cantidad de piezas a procesar: '))
cont = 0
piezaApta = 0

while True:
    if cont == 0:
        cont = 1
    else:
        cont += 1 
        
    
    if cantidad >= cont:                   
        longitud = float(input(f'Ingrese la longitud de la pieza {cont}: '))
        if (longitud >= 1.20) & (longitud <= 1.30):
            piezaApta += 1
    else:
        print(f'Cantidad de piezas aptas son: {piezaApta}')
        break