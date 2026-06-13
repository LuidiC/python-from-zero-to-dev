# Desafio 16
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
print('=' * 5  + ' DESAFIO 16 ' + '=' * 5)

from math import trunc

num = float(input('Digite um número: '))
print(f'O número {num} tem a parte inteira {trunc(num)}')

