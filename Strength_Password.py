import re

print('\033[96m' + 'Strength Password' + '\033[0m')


forma = '\033[91m' + '\033[1m' + '\033[4m'

cont = 0

while True:
    Pass = input('Your Password: ')
    if not re.search('\s', Pass):
        break
    else:
        print("The password can't contain spaces!")

if len(Pass) < 7:
    cont += 1
    print(forma + 'The password should contain 7 or more characters' + '\033[0m')
if not any(char.isdigit() for char in Pass):
    cont += 1
    print(forma + 'The password should have at least one number' + '\033[0m')
if not any(char.isupper() for char in Pass):
    cont += 1
    print(forma + 'The password should have at least one letter in CAPS' + '\033[0m')
if not any(char.islower() for char in Pass):
    cont += 1
    print(forma + 'The password should have at least one lowercase letter' + '\033[0m')
if not re.search("[^a-zA-Z0-9s]", Pass):
    cont += 1
    print(forma + 'The password should have at least one special character' + '\033[0m')
    
if cont == 0:
    print('\033[92m' + 'Your password is strong' + '\033[0m')
elif cont == 1 or cont == 2:
    print('\033[93m' + 'Your password is medium' + '\033[0m')
else:
    print('\033[91m' + 'Your password is weak' + '\033[0m')