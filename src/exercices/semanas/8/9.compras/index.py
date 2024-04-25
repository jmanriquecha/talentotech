"""Compras
Enunciado
Realizar un programa que solicite al usuario el valor de cada una de las compras(No sabemos cuántas compras hizo), si ingresa valores negativos no tomarlo en cuenta y volver a pedirlo, que termine cuando se digite el monto=0 e imprima el total de las compras realizadas
Dificultad
Media

Instrucciones"""

articulo = 1
total = 0

while True:
    valor = float(input(f'Por favor digite el valor de la compra: {articulo} $ '))
    if valor > 0:
        total += valor
        articulo += 1        
    elif valor == 0:
        print(f'Valor total de la compra: $ {total}')
        break
    else:
        print('¡Ha ingresado un valor negativo, por favor intente nuevamente!')
        