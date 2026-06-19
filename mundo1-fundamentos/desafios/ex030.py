# Desafio 30
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
print('=' * 5  + ' DESAFIO 30 ' + '=' * 5)

num = int(input('Digite um número inteiro: '))
          
if num  % 2 == 0:
  print(f'O número {num} é PAR.')
else:
  print(f'O número {num} é ÍMPAR') 