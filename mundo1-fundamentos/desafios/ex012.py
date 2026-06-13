# Desafio 12
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. 
print('=' * 5  + ' DESAFIO 12 ' + '=' * 5)

preco_produto = int(input('Qual o preço do produto? '))
preco_desconto = preco_produto - (preco_produto * 0.05)
print(f'O preço do produto com desconto de 5% é de R$ {preco_desconto}')

