import os
os.system('clear')

###
# EJERCICOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.

# print("\nEjercicio 1:")
# numeros = [1,2,3,4,5]
# numeros.append(6)
# numeros.insert(2, 10)
# numeros[0] = 0
# print(numeros)

# print("\nEjercicio 2:")
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# lista_a.extend(lista_b)
# lista_a.remove(1)
# print(lista_a.pop(3))
# lista_b.clear()
# print(lista_a, lista_b)

# print("\nEjercicio 3:")
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# del numeros[2:5]
# print(numeros)

# print("\nEjercicio 4:")
# numeros = [5, 2, 8, 1, 9, 4, 2]
# numeros.sort()
# cantidad_dos = numeros.count(2)
# is7 = 7 in numeros
# print(f"Lista ordenada: {numeros}") 
# print(f"Cantidad de 2: {cantidad_dos}") 
# print(f"Esta el 7?: {is7}")

# print("\nEjercicio 5:")
# original = [1,2,3]
# copia_1 = original[:]
# copia_2 = original.copy()
# referencia = original
# referencia[0] = 10

# print(f"Original: {original}")      
# print(f"Copia 1 (slicing): {copia_1}")
# print(f"Copia 2 (copy()): {copia_2}") 
# print(f"Referencia: {referencia}") 

print("\nEjercicio 6:")
strings = ["Manzana", "pera", "BANANA", "naranja"]
strings.sort(key=str.lower)
print(strings)