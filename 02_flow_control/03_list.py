###
"""
This script demonstrates the creation, access, slicing, and modification of lists in Python.
The script includes the following sections:
1. Creation of lists:
  - Integer list
  - String list
  - Mixed list
  - Empty list
  - List of lists
2. Accessing elements by index:
  - Accessing elements of a list
  - Accessing elements of a list of lists
3. Slicing lists:
  - Slicing with start and end indices
  - Slicing with start index only
  - Slicing with end index only
  - Copying a list using slicing
  - Slicing with step
4. Modifying elements:
  - Changing an element by index
  - Extending a list with additional elements
"""
# 03 - Listas
# Las listas son un tipo de datos que nos permite almacenar varios valores en una sola variable.
# Las listas son mutables, es decir, que podemos modificarlas una vez creadas.
###
import os
os.system('clear')

# Creación de una lista
print('\nCreación de una lista')
mi_lista = [1, 2, 3, 4, 5] # Lista de enteros
lista2 = ['a', 'b', 'c', 'd', 'e'] # Lista de cadenas
lista3 = [1, 'a', 2, 'b', 3, 'c'] # Lista mixta

lista_vacia = [] # Lista vacía
lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Lista de listas

print(mi_lista)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)

# Acceso a los elementos por indice
print('\nAcceso a los elementos de una lista')
print(mi_lista[0]) # 1 - base 0
print(lista2[1]) # 2
print(lista3[-1]) # c - último elemento

print('\nAcceso a los elementos de una lista de listas')
print(lista_de_listas[0]) # [1, 2, 3]
print(lista_de_listas[1][1]) # 5

# Slicing de listas 
print('\nSlicing de listas')
print(mi_lista[1:3]) # [2, 3] - desde el indice 1 hasta el 3
print(lista2[:3]) # ['a', 'b', 'c'] - desde el inicio hasta el indice 3
print(lista3[3:]) # ['b', 3, 'c'] - desde el indice 3 hasta el final
print(lista3[:]) # [1, 'a', 2, 'b', 3, 'c'] copia de la lista

# Hay mas magia
# print(mi_lista[desde:hasta:salto]) # [2, 4, 6, 8, 10]
print(mi_lista[1:5:2]) # [2, 4]
print(mi_lista[::2]) # para devoler los elementos en posiciones pares
print(mi_lista[::-1]) # para devolver la lista en orden inverso

# Modificación de elementos
print('\nModificación de elementos')
mi_lista[0] = 10
print(mi_lista) # [10, 2, 3, 4, 5]
mi_lista += [6, 7, 8, 9, 10]

# Recuperar longitud de una lista
print('\nLongitud de una lista')
print( 'Longitud de la lista:',len(mi_lista)) # 10