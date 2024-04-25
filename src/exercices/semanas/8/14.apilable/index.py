"""Apilable
Enunciado
Apilable:En la tienda Manaure es tradición exhibir las latas de mermelada apiladas de forma triangular, en la punta del triangulo 1 lata, bajando al siguiente nivel dos latas, al siguiente 3 latas y así sucesivamente, por ejm 6 latas se presentarían * * * *** En la tienda tienen grandes problemas para realizar los pedidos de latas, ya que no todo número de latas se puede apilar triangularmente. Por ejemplo, 8 latas no se pueden apilar. Crea un programa, en el que dado un número natural introducido por el usuario, comprueba si es adecuado o no para apilar
Dificultad
Media

Instrucciones"""

def isTriangular(num):
    if (num < 0):
        return False
    
    sum, n = 0, 1 
    while(sum <= num):
     
        sum = sum + n
        if (sum == num):
            return True
        n += 1 
    return False

while True:
    n = int(input("Introduce la altura del triángulo (entero positivo): "))

    if not isTriangular(n):
        print(f"El número {n} no es un triangular")
        continue
        
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        print("")
    break

