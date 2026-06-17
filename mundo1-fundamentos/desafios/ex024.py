# Desafio 24
# Cie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
print('=' * 5  + ' DESAFIO 24 ' + '=' * 5)

city = input('Digite o nome de uma cidade: ').strip().upper()
if 'SANTO' in city:
    print('A cidade começa com "SANTO".')
else:
    print('A cidade não começa com "SANTO".')
