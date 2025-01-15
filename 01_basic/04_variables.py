my_name = 'gabo'
"""
This script demonstrates basic Python variable usage and conventions.
Variables:
  my_name (str): A string variable representing a name.
  age (int): An integer variable representing age.
  name (str): A dynamically typed variable that changes type.
  mi_nombe_de_variable (str): A variable following snake_case naming convention.
  miNombreDeVariable (str): A variable following camelCase naming convention.
  MiNombreDeVariable (str): A variable following PascalCase naming convention.
  minombredevariable (str): A variable with no separation between words.
  mi_nombre_de_variable_123 (str): A variable with numbers included in the name.
  MI_CONSTANTE (float): A constant variable following UPPER_CASE naming convention.
  is_user_logged_in (bool): A boolean variable with type hinting.
Demonstrates:
  - Dynamic typing in Python.
  - Strong typing in Python.
  - f-string for formatted string literals.
  - Multiple variable assignment.
  - Variable naming conventions.
  - Invalid variable names and reserved keywords.
"""
# print(my_name)

age = 32
# print(age)

age = 39
# print(age)

# Tipado dinamico: el tipo de dato se determina en tiempo de ejecucion. No tienes que declararlo explicitamente

name = 'midudev'
# print(type(name))

name = 32
# print(type(name))

# Tipado fuerte: Py no realiza conversiones de tipos automaticamente
# print(10 + '2')

# f-string (literal de cadena de formato) - Py 3.6
print(f'hola {my_name}, tengo {age} años')

# No es recomndado asginar este tipo de variables
name, age, city = 'Gabriel', 22, 'Santiago'

# Convenciones de nombres de variables - snake_case
mi_nombe_de_variable = 'ok'

miNombreDeVariable = 'ko'
MiNombreDeVariable = 'ko'
minombredevariable = 'ko'
mi_nombre_de_variable_123 = 'ok'

MI_CONSTANTE = 3.14 # No hay const en Py pero se puede simular | UPPER_CASE ----> constante

# Nombres no validos, incluyendo palabras reservadas
# 1212333_variable = 'ko'
# mi-variable = 'ko'
# mi variable = 'ko'

# True = False
# Palabras reservadas en Py 3 [{False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield}]

is_user_logged_in: bool = True
print(is_user_logged_in)

is_user_logged_in = 42
print(is_user_logged_in)

name: str = 'Gabriel'