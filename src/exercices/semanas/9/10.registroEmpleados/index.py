"""Registro de empleados
Enunciado
Registro de Empleados: Crea un programa que permita gestionar el registro de empleados de una empresa. El programa debe tener un menú con las opciones: añadir empleado, mostrar todos los empleados, y salir. Cada empleado debe tener un nombre, un salario y un cargo. Implementa el programa de manera que el usuario pueda realizar múltiples acciones antes de decidir salir.
Dificultad
Media

Instrucciones"""

db_empleados = []

def registroEmpleados():
    print('GESTIÓN DE EMPLEADOS: ')
    
    while True:    
        print('Para salir escriba (0)')
        accion = int(input('(1) Añadir, (2) Mostra\n'))
        if accion == 0:
            print('Presionaste salir')
            break
        elif accion == 1:
            nombre = input('Ingrese el nombre: ')
            salario = input('Ingrese el salario : $')
            cargo = input('Ingrese el cargo: ')
            agregarEmpleado(nombre,salario,cargo)
            print('Empleado se agrego correctamente: ')
        elif accion == 2:
            print('Lista de empleados')
            print(mostrarEmpleados())
        else:
            print('No has ingresado un opción válida')
        
            
    
def agregarEmpleado(nombre, salario, cargo):
    nuevo = {
        'nombre' : nombre,
        'salario' : salario,
        'cargo' : cargo
        }
    db_empleados.append(nuevo)

def mostrarEmpleados():
    return db_empleados
    
if __name__ == "__main__":
    registroEmpleados()