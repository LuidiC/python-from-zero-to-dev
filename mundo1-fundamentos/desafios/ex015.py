# Desafio 15
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por Km rodado.
print('=' * 5  + ' DESAFIO 15 ' + '=' * 5)

dias_uso = int(input('Quantos dias alugados? '))
km_rodados = float(input('Quantos Km rodados? '))
total_pagar = (dias_uso * 60) + (km_rodados * 0.15)
print(f'Você deve pagar pelo aluguel do carro um total de R${total_pagar:.2f}')