# Desafio 29
'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada Km acima do limite.
'''
print('=' * 5  + ' DESAFIO 29 ' + '=' * 5)

velocidade = float(input('Digite a velocidade do carro em Km/h: '))
if velocidade > 80:
  multa = velocidade - 80
  valor_multa = multa * 7
  print(f'Você foi multado por ultrapassar o limite de velocidade permitido.\nA multa é de R${valor_multa:.2f}.')