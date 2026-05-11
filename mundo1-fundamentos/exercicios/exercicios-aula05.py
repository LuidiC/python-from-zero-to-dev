# Declare 4 tipos de variável diferentes e exiba no terminal a que classe elas pertencem.  
exemplo1 = 8.6
exemplo2 = 8
exemplo3 = True
exemplo4 = 'nome'
print(type(exemplo1), type(exemplo2), type(exemplo3), type(exemplo4))

# Peça para o usuário 1 número e avalie se esse número é numérico, se é letra ou não e se tem letra ou número. 
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
soma = num1 + num2
num3 = input('Digite outro número: ')
print(f'A soma entre {num1} e {num2} vale {soma}')
print(num3.isnumeric())
print(num3.isalpha())
print(num3.isalnum())

