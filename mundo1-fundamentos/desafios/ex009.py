# Desafio 09
# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada. 
print('=' * 5  + ' DESAFIO 09 ' + '=' * 5)

num = int(input("Escreva um número: "))
print('-' * 12)
for i in range(11): 
    print(f'{num} X {i} = {num * i}')
print('-' * 12)

