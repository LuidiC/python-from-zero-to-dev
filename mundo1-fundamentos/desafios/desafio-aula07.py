# Desafio 1
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor. 
num = int(input('Escreva um número: '))
print(f'O número antecessor do {num} é {num-1}\ne\no número sucessor é {num + 1}')

# Desafio 2
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
num2 = int(input('Escreva um número: '))
print(f'O dobro de {num2} é {num2*2}')
print(f'O triplo de {num2} é {num2*3}')
print(f'A raiz quadrada de {num2} é {num2 ** (1/2):.2f}')

# Desafio 3
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

aluno1 = int(input('Digite a nota do primeiro aluno: '))
aluno2 = int(input('Digite a nota do segundo aluno: '))
media_alunos = (aluno1 + aluno2)/2
print(f'A média das notas dos alunos é de {media_alunos:.2f}')

# Desafio 4
# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
qtd_metros = int(input('Digite quantos metros você quer converter: '))
print(f'{qtd_metros} é igual a {qtd_metros * 100} centímetros.')
print(f'{qtd_metros} é igual a {qtd_metros * 1000} milímetros.') 

# Desafio 5
# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada. 
num = int(input("Escreva um número: "))
for i in range(11): 
    print(f'{num} * {i} = {num * i}')

# Desafio 6
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
valor_real = int(input('Quantos reais você tem na carteira? '))
dolar = valor_real/4.91 #Valor do dólar no dia 11/05/2026
print(f'Com {valor_real} reais você pode compra {dolar:.2f} dólares.')

# Desafio 7
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2
      
altura = int(input('Escreva a altura da parede em metros: '))
largura = int(input('Escreva a largura da parede em metros: '))
area = altura * largura
qtd_tinta = area/2
print(f'A área dessa parede é igual a {area} m^2.')
print(f'A quantidade de tinta necssária para pintar essa parede é de {qtd_tinta} litros.')

# Desafio 8
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. 
preco_produto = int(input('Qual o preço do produto? '))
preco_desconto = preco_produto - (preco_produto * 0.05)
print(f'O preço do produto com desconto de 5% é de R$ {preco_desconto}')

# Desafio 9
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento. 
salario = int(input('Qual é o seu salário? '))
novo_salario = salario + (salario * 0.15)
print(f'Seu novo salário com 15% de aumento é de R$ {novo_salario:.2f}!')