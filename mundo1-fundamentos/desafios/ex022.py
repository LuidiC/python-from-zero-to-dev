''' 
 Desafio 22
 Crie um programa que leia o nome completo de uma pessoa e mostre:

- O nome com todas as letras maiúsculas
- O nome com todas as letras minúsculas
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome  
'''
print('=' * 5  + ' DESAFIO 22 ' + '=' * 5)

nome = input('Qual é seu nome? ')
print(nome.upper())
print(nome.lower())
nome_sem_espaço = nome.strip()
print(f'Seu nome possui {len(nome_sem_espaço)} letras')
lista_nome = nome.split(' ') 
print(f'O seu primeiro nome tem {len(lista_nome[0])} letras')
