"""
Nomina
Enunciado
Nomina: En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.
Dificultad
Media

Instrucciones
"""

empleados = int(input('Ingrese el número de empleados que laboran en la empresa: '))
importe = 0
min300 = 0
max300 = 0

for n in range(empleados):
    n += 1
    sueldo = float(input(f'Sueldo del empleado {n} $ '))
    if (sueldo > 0) & (sueldo < 100):
        importe += sueldo        
    elif (sueldo >= 100) & (sueldo <= 300):
        importe += sueldo
        min300 += 1
    else:
        importe += sueldo
        max300 += 1
        
print(f'El importe total de la empresa es: {importe}, {min300} empleados cobran entre $100 y $300; {max300} empleados cobran más de $300')
    
