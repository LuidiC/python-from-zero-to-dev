# Desafio 33 
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor 
print('=' * 5  + ' DESAFIO 33 ' + '=' * 5)

maior = None
menor  = None 

for i in range (1,4):
  num = int(input(f'Digite o {i}º numero : '))
  if maior == None or num > maior:
    maior = num 
  if menor == None or num < menor:
    menor = num 
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')
  
