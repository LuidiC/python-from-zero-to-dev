# Desafio 35
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo 
print('=' * 5  + ' DESAFIO 35 ' + '=' * 5)

r1 = float(input('Escreva o comprimento da 1º reta: '))
r2 = float(input('Escreva o comprimento da 2º reta: '))
r3 = float(input('Escreva o comprimento da 3º reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print(f'As retas de comprimentos:\nComprimento da 1º reta: {r1}\nComprimento da 2º reta: {r2}\nComprimento da 3º reta: {r3}\nPODEM formar um triângulo!')
else:
    print(f'As retas de comprimentos:\nComprimento da 1º reta: {r1}\nComprimento da 2º reta: {r2}\nComprimento da 3º reta: {r3}\nNÃO PODEM formar um triângulo!')