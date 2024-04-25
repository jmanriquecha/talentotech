"""Dias de la semana
Enunciado
Realizar un programa que pida al usuario digitar un día de la semana
* Si es lunes, sábado o domingo imprimir el día de la semana y un mensaje
* Si es viernes imprima el día de la semana y “Ya vemos cerca el fin de semana”
De lo contrario imprima “Avancemos que ya es”, día de la semana
Dificultad
Media"""

dia = input('Por favor ingrese el un día de la semana: ').lower()

if dia in ['lunes', 'sabado', 'sábado', 'domingo']:
    if(dia == 'sabado'):
        dia = 'sábado'
    msg = 'Hoy es un día fabuloso por que es: '
elif dia == 'viernes':
    msg = 'Ya vemos cerca el fin de semana'
elif dia in ['martes', 'miércoles', 'miercoles', 'jueves']:
    if(dia == 'miercoles'):
        dia = 'miércoles'
    msg = 'Avancemos que ya es'
else:
    msg = 'No has ingresado un día valido: '
   
print(f'{msg} {dia.capitalize()}')