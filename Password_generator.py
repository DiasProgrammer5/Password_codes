import random
import string

print('\033[1m' + '\033[96m' + 'Random Password' + '\033[0m')
num_min = 7

try: 
    numbers = int(input('Coloca o nº de carateres que seja superior ou igual {}: '.format(num_min)))
    
    if numbers >= num_min:
        print('\033[92m' + 'A tua palavra-passe: ' + '\033[0m')

        chars = string.printable.strip()

        password = ''
        for x in range(numbers):
            password += random.choice(chars)
            
        print(password)
    else: 
        print('\033[91m' + 'Erro, o nº tem de ser maior ou igual a {}'.format(num_min) + '\033[0m')
except ValueError:
    print('\033[91m' + 'Erro, tem de colocar um nº válido' + '\033[0m')
