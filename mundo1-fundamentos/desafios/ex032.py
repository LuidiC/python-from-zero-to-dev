# Desafio 32
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto 
print('=' * 5  + ' DESAFIO 32 ' + '=' * 5)

ano = int(input('Digite o ano que será avaliado: '))
if ano % 4 == 0 and ano % 100 != 0:
  print(f'O ano {ano} é bissexto!')
else:
  print(f'O ano {ano} não é bissexto!')