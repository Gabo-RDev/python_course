###
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