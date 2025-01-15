nombre = input('Hola, ¿cómo te llamas?\n')
"""
This script interacts with the user to gather personal information and display it back.
Functions:
  None
Variables:
  nombre (str): The name of the user.
  age (str): The age of the user.
  country (str): The country the user is from.
  city (str): The city the user is from.
Workflow:
  1. Prompts the user for their name and greets them.
  2. Prompts the user for their age and calculates their age next year.
  3. Prompts the user for their country and city of residence and displays the information.
"""
print(f'Hola, {nombre}, encantado de conocerte.')

age = input('¿Cuántos años tienes?\n')
print(f"Dentro de un año tendrás {int(age) + 1} años.")

print('Obtener múltiples valores en una sola línea:')
country, city = input('¿De qué país y ciudad eres?\n').split()

print(f'Vives en {city}, {country}.')