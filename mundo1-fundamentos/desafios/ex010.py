# Desafio 10
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
print('=' * 5  + ' DESAFIO 10 ' + '=' * 5)

valor_real = int(input('Quantos reais você tem na carteira? '))
dolar = valor_real/4.91 #Valor do dólar no dia 11/05/2026
print(f'Com {valor_real} reais você pode compra {dolar:.2f} dólares.')

