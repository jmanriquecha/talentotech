""" 
Base de datos de clientes
Enunciado
Base de datos de clientes: Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIT, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferencial), dónde preferencial tendrá el valor True si se trata de un cliente preferencial. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferenciales, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:
1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
2. Preguntar por el NIT del cliente y eliminar sus datos de la base de datos.
3. Preguntar por el NIT del cliente y mostrar sus datos.
4. Mostrar lista de todos los clientes de la base datos con su NIT y nombre.
5. Mostrar la lista de clientes preferenciales de la base de datos con su NIT y nombre.
6. Terminar el programa.
Dificultad
Media

Instrucciones
"""

clientes = {}

# Esta función se encarga de buscar si un cliente existe en la base de datos clientes y retorna el nit
def buscarCliente(nit):
    result = False
    for cliente in clientes:
        if(cliente == nit):
            result = cliente
    return result

def nuevoCliente(nit, nombre, direccion, telefono, correo, preferencial = False):
    existeCliente = buscarCliente(nit)
    if(existeCliente == False):        
        nuevo = {
            "nombre":nombre,
            "direccion":direccion,
            "telefono":telefono,
            "correo":correo,
            "preferencial":preferencial
        }
        clientes[nit] = nuevo
    else:
        print(f'El cliente con NIT {existeCliente} ya existe en la base de datos! ')
    
# Muestra un cliente en especifico
def mostrarCliente(nit):
    existeCliente = buscarCliente(nit)
    if not existeCliente == False:
        return clientes[existeCliente]
    else:
        return f'El cliente con NIT: "{nit}" no existe en la base de datos! '

# Eliminar cliente
def eliminarCliente(nit):
    existeCliente = buscarCliente(nit)
    if not existeCliente == False:
        clientes.pop(nit)
        return True
    else:
        return f'El cliente con NIT: "{nit}" no existe en la base de datos! '
    
# Listar todos los clientes
def listarClientes():
    return clientes

# Listar clientes preferenciales
def listarClientesPreferenciales():
    result = []
    for cliente in clientes:
        if(clientes[cliente]['preferencial'] != False):
            result.append(f'{cliente}: {clientes[cliente]}')   
    return result     

# Ejecutar programa
while True:
    opcion = int(input('\n\nSeñor usuario por favor elija una opción: \n(1) Añadir cliente, \n(2) Elimiar cliente, \n(3) Mostrar cliente, \n(4) Listar todos los clientes, \n(5) Listar clientes preferenciales, \n(6) Terminar: \n\n' ))
    
    if opcion == 1:
        # Solicita datos del cliente
        nit = input('Ingrese el NIT: ')
        nombre = input('Ingrese el Nombre: ')
        direccion = input('Ingrese la dirección: ')
        telefono = input('Ingrese el teléfono: ')
        email = input('Ingrese el Email: ')        
        preferencial = int(input('Ingrese (1). Si es preferencial, (2). si no es preferencial: '))
        if(preferencial == 1):
            preferencial = True
        else:
            preferencial = False
        agregar = nuevoCliente(nit, nombre, direccion, telefono, email, preferencial)
        print(agregar)
    elif opcion == 2:
        nit = input('Ingrese el NIT del usuario que quiere elimiar: ')
        eliminar = eliminarCliente(nit)
        if(eliminar):
            print(eliminar)
    elif opcion == 3:
        nit = input('Ingrese el NIT del usuario que quiere mostrar: ')
        mostrar = mostrarCliente(nit)
        print(mostrar)
    elif opcion == 4:
        listar = listarClientes()
        print(listar)
    elif opcion == 5:
        preferenciales = listarClientesPreferenciales()
        print(preferenciales)
    elif opcion == 6:
        print('Programa terminado! ')
        break
    else:
        print('No ha ingresado una opción valida! ')
