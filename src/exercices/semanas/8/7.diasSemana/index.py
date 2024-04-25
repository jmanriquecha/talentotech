"""Dias de la semana
Enunciado
Realizar un programa que pida al usuario digitar un día de la semana
* Si es lunes, sábado o domingo imprimir el día de la semana y un mensaje
* Si es viernes imprima el día de la semana y “Ya vemos cerca el fin de semana”
De lo contrario imprima “Avancemos que ya es”, día de la semana
Dificultad
Media"""

dia = input('Por favor ingrese el un día de la semana: ')
dia = dia.lower()

if(dia == 'lunes') | (dia == 'sabado') | (dia == 'sábado') | (dia == 'domingo'):
    msg = f'¡{dia.capitalize()} es un día fabuloso!'
elif dia == 'viernes':
    msg = f'{dia.capitalize()} Ya vemos cerca el fin de semana'
elif (dia == 'martes') | (dia == 'miércoles') | (dia == 'miercoles') | (dia == 'jueves'):
    msg = f'Avancemos que ya es {dia.capitalize()}'
else:
    msg = 'No has ingresado un día valido: '
   
print(msg)