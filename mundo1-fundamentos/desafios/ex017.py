# Desafio 17
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot

print('=' * 5  + ' DESAFIO 17 ' + '=' * 5)

cateto_oposto = float(input('Digite o cateto oposto do triângulo retângulo: '))
cateto_adjacente = float(input('Digite o cateto adjacente do triângulo retângulo: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f'O comprimento da hipotenusa desse triângulo retângulo é igual a {hipotenusa:.2f}')

