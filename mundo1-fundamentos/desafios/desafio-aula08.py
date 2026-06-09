# Desaffio 01 
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. 
from math import trunc

num = float(input('Digite um número: '))
print(f'O número {num} tem a parte inteira {trunc(num)}')

# Desafio 02
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot

cateto_oposto = float(input('Digite o cateto oposto do triângulo retângulo: '))
cateto_adjacente = float(input('Digite o cateto adjacente do triângulo retângulo: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f'O comprimento da hipotenusa desse triângulo retângulo é igual a {hipotenusa:.2f}')

# Desafio 03
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan

angulo = float(input('Digite o valor do ângulo: '))
seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)
print(f'O ângulo {angulo} possui:\nseno = {seno:.2f}\ncosseno = {cosseno:.2f}\ntangente = {tangente:.2f}')

# Desafio 04 
# Um professor quer sortaer um dos seus quatro alunos para apagar o quadro.
import random

nomes_alunos = []
for i in range (1,5):
    aluno = input(f'Digite o nome do aluno {i}: ')
    nomes_alunos.append(aluno)

sorteado = random.choice(nomes_alunos)
print(f'O aluno sorteado foi {sorteado}')

# Desafio 05
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada 
import random 

total_alunos = []
for i in range(1,5):
    nome_aluno = input(f'Digite o nome do aluno {i}: ')
    total_alunos.append(nome_aluno)

random.shuffle(total_alunos)
print(f'A ordem de sorteio dos alunos foi:\n {total_alunos}')

# Desafio 06
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.mixer.init()

pygame.mixer.music.load("sonican-thinking-time-ticking-power-223023.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)