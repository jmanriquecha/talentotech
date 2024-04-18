""" 
Precio de venta
Enunciado
Precio de venta: Dado el valor de un producto, hallar el ingreso general a las ventas y el precio de venta, teniendo en cuenta que Igv= PP*0.19 y PV=PP+Igv
Dificultad
Media

Instrucciones
"""


#Precio de venta
precio_producto = float(input("Ingrese el valor del producto: "))

igv = precio_producto * 0.19
precio_venta = precio_producto + igv

print(f"Ingreso general a las ventas: {precio_venta}")
print(f"Precio de venta: {precio_venta}")