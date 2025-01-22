###
"""
This script demonstrates various list methods in Python.
The following list methods are covered:
- append: Adds an element to the end of the list.
- insert: Adds an element at the specified position.
- extend: Adds multiple elements to the end of the list.
- remove: Removes the first element with the specified value.
- pop: Removes the last element of the list.
- del: Deletes the element at the specified position.
- clear: Removes all elements from the list.
Additionally, the script demonstrates:
- Deleting a range of elements from a list.
- Sorting a list in place and without mutating the original list.
- Sorting a list of strings, including case-insensitive sorting.
- Useful list operations such as getting the length of a list, counting occurrences of an element, and checking for membership.
"""
# 04 Lista de métodos
# Los métodos son funciones que se pueden aplicar a un objeto.
# En Python, los métodos son funciones que pertenecen a un objeto.
###
import os
os.system('clear')

list1 = [1, 2, 3, 4, 5]
list1.append(6) # Agrega un elemento al final de la lista
print(list1)

list1.insert(0, 0) # Agrega un elemento en la posición indicada
print(list1)

list1.extend([7, 8, 9]) # Agrega varios elementos al final de la lista
print(list1)

list1.remove(0) # Elimina el primer elemento con el valor indicado
print(list1)

list1.pop() # Elimina el último elemento de la lista
print(list1)

del list1[-1] # Elimina el elemento en la posición indicada
print(list1)

list1.clear() # Elimina todos los elementos de la lista
print(list1) # []

# Eliminar un rango de elementos
lista = [1, 2, 3, 4, 5]
del lista[1:3]
print(lista) # [1, 4, 5]

# Metodos utiles
print('Ordenar lista mutando la original')
lista3 = [2, 5, 101, 50, 24, 8]
lista3.sort() # Ordena la lista
print(lista3) # [1, 2, 3, 4, 5]

print('Ordenar lista sin mutar la original')
lista4 = [2, 5, 101, 50, 24, 8]
lista4_sorted = sorted(lista4) # Ordena la lista
print(lista4_sorted) # [2, 5, 101, 50, 24, 8]

print('Ordernar una lista de cadenas de texto')
frutas = ['manzana', 'Pera', 'uva', 'Sandia']
sorted_frutas = sorted(frutas)
print(sorted_frutas) # ['Pera', 'Sandia', 'manzana', 'uva'] 

print('Ordenar una lista de cadenas de texto sin importar mayusculas')
sorted_frutas = sorted(frutas, key=str.lower)
print(sorted_frutas) # ['manzana', 'Pera', 'Sandia', 'uva']

# Mas cosas utiles
animals = ['🐶', '🐰', '🐰', '🐰']
print(len(animals)) # 4
print(animals.count('🐰')) # 3
print("🐰" in animals) # True
