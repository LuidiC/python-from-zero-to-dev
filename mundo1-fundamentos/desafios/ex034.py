# Desafio 34
'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
- Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
- Para os inferiores ou iguais, o aumento é de 15%.
'''
print('=' * 5  + ' DESAFIO 34 ' + '=' * 5)

salario = float(input('Qual o valor do seu salário? '))

if salario > 1250:
    aumento = 0.10
else: 
    aumento = 0.15

novo_salario = salario + (salario * aumento) 
print(f'Seu novo salário após o aumento é de R${novo_salario:.2f}!')
