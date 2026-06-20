# Desafio 31
# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas. 
print('=' * 5  + ' DESAFIO 31 ' + '=' * 5)

distancia = int(input('Qual a distância da sua viagem em km? '))
if distancia <= 200:
  preco_passagem = distancia * 0.5
else: 
  preco_passagem = distancia * 0.45
print(f'O preço da sua passagem é de R${preco_passagem:.2f} ')
