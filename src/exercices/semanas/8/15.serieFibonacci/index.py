"""Serie Fibonacci
Enunciado
Serie Fibonacci: Crea un programa que calcule y visualice los elementos de la serie de Fibonacci. Esta serie se define de la siguiente manera:
Fibonacci(0) = 0
Fibonacci(1) = 1
Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
El usuario tan sólo introducirá el número de elementos que quiere visualizar.
Dificultad
Media

Instrucciones"""

#Fibonacci

def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

cantidad_elementos = int(input("Ingrese el número de elementos de la serie Fibonacci: "))
resultado = fibonacci(cantidad_elementos)
print(f"Los primeros {cantidad_elementos} elementos de la serie Fibonacci son: {resultado}")