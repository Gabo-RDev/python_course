###
"""
This script demonstrates various uses of conditional statements in Python.
The script includes examples of:
1. Simple if statements
2. If-else statements
3. If-elif-else statements
4. Multiple conditions using logical operators (and, or, not)
5. Nested conditional statements
Examples:
- Checking if a person is of legal age.
- Grading system based on scores.
- Checking if a person can drive based on age and possession of a driving license.
- Conditional statements for weekend checks.
- Nested conditions to determine if a person can go to a disco based on age and money.
Each section prints the result of the conditional checks to the console.
"""
# 01 - If statement (if, elif, else)
###

import os
os.system('clear')

print('\n Sentecia simple condicional')
edad = 18
if edad >= 18:
  print('Eres mayor de edad')

edad = 15
if edad >= 18:
  print('Eres mayor de edad')
  print('Felicidades!')

print('\n Sentecia condicional con else')
edad = 15
if edad >= 18:
  print('Eres mayor de edad')
  print('Felicidades!')
else:
  print('Eres menor de edad')



print('\n Sentecia condicional con elif')
nota = 7 
if nota >= 9:
  print('Sobresaliente')
elif nota >= 7:
  print('Notable')
elif nota >= 5:
  print('Aprobado')
else:
  print('Reprobado')

print('\n Condiciones multiples')
edad = 25
tiene_carnet = True

if edad >= 18 and tiene_carnet:
  print('Puedes conducir')
else:
  print('POLICIA!!!!')

# Isla Margarita
if edad >= 18 or tiene_carnet:
  print('Puedes conducit en la Isla')
else:
  print('Paga al policia y te deja conducir!!')

# JS -> !
es_fin_de_semana = False
if not es_fin_de_semana:
  print('Venga, que hay trabajar')

print('\n Anidad condicionales')
edad = 20
tiene_dinero = True
if edad >= 20:
  if tiene_dinero:
    print('Puedes ir a la discoteca')
  else:
    print('Quedate en casa')
else: 
  print('No puedes entrar a la disco')

# Mas facil
if edad < 18:
  print('No puedes ir a la disco')
elif tiene_dinero:
  print('Puedes ir a la disco')
else: 
  print('Vete a casa')

print('\nLa condicion ternaria')
edad = 17
mensaje = 'Eres mayor de edad' if edad >= 18 else 'Eres menor de edad'
print(mensaje)