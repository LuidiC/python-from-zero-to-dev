# Desafio 20
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada 
import random 

print('=' * 5  + ' DESAFIO 20 ' + '=' * 5)

total_alunos = []
for i in range(1,5):
    nome_aluno = input(f'Digite o nome do aluno {i}: ')
    total_alunos.append(nome_aluno)

random.shuffle(total_alunos)
print(f'A ordem de sorteio dos alunos foi:\n {total_alunos}')

