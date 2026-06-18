# Desafio 28
'''
Escreva um  programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
import random

print('=' * 5  + ' DESAFIO 28 ' + '=' * 5)
num_sorteado = random.randint(0,5)
num_escolhido = int(input('Escolha um número de 0 a 5: '))
if num_escolhido >=0 and num_escolhido <= 5:
  if num_escolhido == num_sorteado:
    print('Parabéns, você acertou o número!')
  else: 
    print(f'Que pena, você errou! O número sorteado foi {num_sorteado}.')
else:
  print('Número inválido. Por favor, escolha um número de 0 a 5.')
