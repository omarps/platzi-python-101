import random

options = ('piedra', 'papel', 'tijera')
computer_option = random.choice(options)

user = input('¿piedra, papel o tijera? ')
if not user in options:
    print('Por favor, elige una opción válida...')
    exit()