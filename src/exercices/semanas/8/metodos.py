from mis_datos import mi_lista_py

# print(mi_lista_py)
# mi_lista_py.append(1025) #Agrega un nuevo valor al final de la lista

# print(mi_lista_py)

# #Coutn: Devuelve cuantas veces se repite un valor en la lista

# print(mi_lista_py.count(10)) #Busca en la lista cuantas veces aparece un valor

# # len
# print(len(mi_lista_py)) ##Devuelve cuantos elementos tiene la lista

# # Index() devuelve el valor en la posicion con index

# print(mi_lista_py.index(1))

# #remove el elemento de la lista

# mi_lista_py.remove(9)
# print(mi_lista_py)

# ## pop() Eliminamos el elemento ubicado en la posición
# mi_lista_py.pop(2)
# print(mi_lista_py)

# ## extend() une listas

# mi_lista_py.extend(['jaja','esto es nuevo'])
# print(mi_lista_py)


# ## reverse() invierte la lista

# mi_lista_py.reverse()
# print(mi_lista_py)


## sort()

nuevaLista = [1,200,30,40,50,60,70,100]
# print(nuevaLista)
# nuevaLista.sort() ## Por defecto de menor a mayor
# print(nuevaLista)
# nuevaLista.sort(reverse=True) ## de mayor a menor
# print(nuevaLista)

## Parecido al metodo sort()
# print(sorted(mi_lista_py))


nuevaCopia = nuevaLista.copy()
nuevaCopia.append('jaja')
print(nuevaCopia)
print(nuevaLista)


## concatenar

lista1 = [15,25,35,44,55]
lista2= ['Hola', 'saludo']
resultado = lista1.__add__(lista2)
print(resultado)


formato = ['sdfl']
resultado = lista1.__format__(formato)
print(resultado)