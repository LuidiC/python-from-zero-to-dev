# Desafio 11
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2
print('=' * 5  + ' DESAFIO 11 ' + '=' * 5)

altura = int(input('Escreva a altura da parede em metros: '))
largura = int(input('Escreva a largura da parede em metros: '))
area = altura * largura
qtd_tinta = area/2
print(f'A área dessa parede é igual a {area} m^2.')
print(f'A quantidade de tinta necssária para pintar essa parede é de {qtd_tinta} litros.')

