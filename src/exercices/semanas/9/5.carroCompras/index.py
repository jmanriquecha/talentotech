""" 
Cesta de compras
Enunciado
Cesta de compras: Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar ingresando la palabra “FIN”. Después se debe mostrar por pantalla la lista de la compra y el coste total, de la siguiente manera
Articulo 1 Valor
Articulo 2 Valor
Articulo 3 Valor
TOTAL VALOR
Dificultad
Media

Instrucciones
"""

carShoping = []

def addCar(producto, precio):
    item = {'producto':producto, 'precio': precio}
    carShoping.append(item)
    
def listaCompra():
    total = 0
    for item in carShoping:
        print(f'{item['producto']} ${item['precio']}')
        total += item['precio']
    print(f'\nTOTAL: ${total}')

while True:
    articulo = input("Ingrese el nombre del artículo (o 'FIN' para finalizar): ")
    
    if articulo.lower() != 'fin':
        precio = float(input(f'Ingrese precio para "{articulo}": '))
        addCar(articulo, precio)
    else:
        print('\n¡Haz finalizado la compra!\n')
        listaCompra()
        break
    
    
# cesta = {}
# while True:
#     articulo = input("Ingrese el nombre del artículo (o 'FIN' para finalizar): ")
#     if articulo.upper() == "FIN":
#         break
#     precio = float(input(f"Ingrese el precio de {articulo}: "))
#     cesta[articulo] = precio

# print("\nLista de la compra:")
# total = 0
# for articulo, precio in cesta.items():
#     print(f"{articulo}\t{precio}")
#     total += precio

# print(f"\nTOTAL\t{total}")