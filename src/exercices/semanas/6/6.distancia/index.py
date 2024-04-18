""" 
Distancia
Enunciado
Distancia: Se desea calcular la distancia recorrida(m) por un móvil que tiene velocidad constante(m/s) durante un tiempo t(s),considera que es MRU(Movimiento rectilíneo uniforme), teniendo en cuenta que la fórmula de V en MRU es V=D/T
"""

#Distancia
velocidad = float(input("Ingrese la velocidad en m/s: "))
tiempo = float(input("Ingrese el tiempo en segundos: "))

distancia = velocidad * tiempo
print(f"La distancia recorrida es: {distancia} metros")