import os
os.system('clear')
###
# EJERCICOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)



# Ejercicio 1: Determinar el mayor de dos números
###
#if num1 > num2:
#    print(f"{num1} es mayor que {num2}")
#elif num2 > num1:
#    print(f"{num2} es mayor que {num1}")
#else:
#    print("Los números son iguales")
###

# Ejercicio 2: Calculadora simple
#print('\nCalculadora simple')
#num1 = float(input('Introduce el primer número: '))
#num2 = float(input('Introduce el segundo número: '))
#op = (input('Introducir un operador (+, -, *, /): '))
#
#if op == '+':
#  resultado = num1 + num2
#elif op == '-':
#  resultado = num1 - num2
#elif op == '*':
#  resultado = num1 * num2
#elif op == '/':
#  if num2 == 0:
#    print('No se puede dividir entre 0')
#    resultado = None
#  else:
#    resultado = num1 / num2
#else:
#  print('Operador no válido')
#  resultado = None
#
#if resultado is not None:
#  print(f'El resultado es: {resultado}')

# Ejercicio 3: Año bisiesto
#print("\nDeterminar si es un year bisiesto o no:")
#year = int(input("Introduce un año: "))
#
#if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#  print('Es un year bisiesto')
#else:
#  print('No es un year bisiesto')

# Ejercicio 4: Categorizar edades
#print('\n Categorizar edades')
#edad = int(input('Cual es tu edad? '))
#
#if 0 <= edad <= 2:
#  print('Eres un crio')
#elif edad >= 3 and edad <= 12:
#  print('Eres un niño')
#elif edad >= 13 and edad <= 17:
#  print('Eres un adolescente')
#elif edad >= 18 and edad <= 64:
#  print('Eres un adulto')
#elif edad >= 65:
#  print('Eres un adulto mayor')
#else:
#  print('Edad no valida')
