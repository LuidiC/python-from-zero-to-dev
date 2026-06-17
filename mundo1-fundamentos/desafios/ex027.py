# Desafio 27
'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex: ANa Maria de Souza 
primeiro: Ana 
último: Souza
'''
print('=' * 5  + ' DESAFIO 27 ' + '=' * 5)

name = input('Digite seu nome completo: ')
lista_name = name.split(' ')
print(lista_name)
first_name = lista_name[0]
last_name = lista_name[len(lista_name)-1] 
print(f'Primeiro nome: {first_name}')
print(f'Último nome: {last_name}')