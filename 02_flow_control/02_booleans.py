# Booleans in Python
"""
This script demonstrates the use of boolean values, boolean expressions, string comparisons, 
logical operators, and truth tables in Python.
The script includes the following sections:
1. Boolean values: Assigns True and False to variables.
2. Boolean expressions: Demonstrates comparison operators (>, <, ==, !=, >=, <=) with integers.
3. String comparisons: Compares strings using comparison operators (==, !=, >, <).
4. Logical operators: Demonstrates logical operators (and, or, not) with boolean values.
5. Truth table: Prints the truth table for logical operators (and, or, not).
Each section prints the results of the operations to the console.
"""
import os
os.system('clear')
# Boolean values
is_true = True
is_false = False

# Boolean expressions
print('\nOperadores de comparacion')
print('5 > 3:', 5 > 3)  # True 
print('5 < 3:', 5 < 3)  # False
print('5 == 5', 5 == 5)  # True
print('5 != 3') # True
print('5 >= 3') # True
print('5 <= 3') # False

# Comparacion de strings
print('\nComparacion de strings')
print('hola' == 'hola')  # True
print('hola' == 'adios')  # False
print('hola' != 'adios')  # True
print('hola' > 'adios')  # True
print('hola' < 'adios')  # False
print('manzana' > 'mandar' )  # False

# Operadores logicos
print('\nOperadores logicos')
print(True and False)  # False
print(True or False)  # True
print(not True)  # False

# Tabla de verdad
print('\nTabla de verdad')
print('True and True:', True and True)
print('True and False:', True and False)
print('False and True:', False and True)
print('False and False:', False and False)
print('not:')
print('not True:', not True)
print('not False:', not False)