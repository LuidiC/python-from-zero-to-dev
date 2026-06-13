# Desafio 13
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento. 
print('=' * 5  + ' DESAFIO 13 ' + '=' * 5)

salario = int(input('Qual é o seu salário? '))
novo_salario = salario + (salario * 0.15)
print(f'Seu novo salário com 15% de aumento é de R$ {novo_salario:.2f}!')

