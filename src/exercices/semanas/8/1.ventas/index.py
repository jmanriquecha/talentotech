"""
Ventas
Enunciado
Ventas: Realizar un programa que solicite las ventas de 3 productos e imprima: El producto más costoso, el producto más económico y la media de los productos
Dificultad
Media
"""
#Ventas

ventas = [float(input(f"Ingrese las ventas del producto {i + 1}: ")) for i in range(3)]

producto_mas_costoso = max(ventas)
producto_mas_economico = min(ventas)
media_ventas = sum(ventas) / len(ventas)

print(f"Producto más costoso: {producto_mas_costoso}")
print(f"Producto más económico: {producto_mas_economico}")
print(f"Media de las ventas: {media_ventas}")