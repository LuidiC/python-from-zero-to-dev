# Desafio 07
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
print('=' * 5  + ' DESAFIO 07 ' + '=' * 5)

aluno1 = int(input('Digite a nota do primeiro aluno: '))
aluno2 = int(input('Digite a nota do segundo aluno: '))
media_alunos = (aluno1 + aluno2)/2
print(f'A média das notas dos alunos é de {media_alunos:.2f}')

