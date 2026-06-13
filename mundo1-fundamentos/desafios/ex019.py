# Desafio 19 
# Um professor quer sortaer um dos seus quatro alunos para apagar o quadro.
import random

print('=' * 5  + ' DESAFIO 19 ' + '=' * 5)

nomes_alunos = []
for i in range (1,5):
    aluno = input(f'Digite o nome do aluno {i}: ')
    nomes_alunos.append(aluno)

sorteado = random.choice(nomes_alunos)
print(f'O aluno sorteado foi {sorteado}')

