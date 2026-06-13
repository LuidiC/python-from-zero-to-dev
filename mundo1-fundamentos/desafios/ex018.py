# Desafio 18
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan

print('=' * 5  + ' DESAFIO 18 ' + '=' * 5)

angulo = float(input('Digite o valor do ângulo: '))
seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)
print(f'O ângulo {angulo} possui:\nseno = {seno:.2f}\ncosseno = {cosseno:.2f}\ntangente = {tangente:.2f}')

