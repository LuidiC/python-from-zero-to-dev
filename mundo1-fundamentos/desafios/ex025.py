# Desafio 25
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
print('=' * 5  + ' DESAFIO 25 ' + '=' * 5)

name = input('Digite o seu nome: ').upper()
if 'SILVA' in name:
  print(f'O nome "{name}" contém "SILVA".')
else:
  print(f'O nome "{name}" não contém "SILVA".')
