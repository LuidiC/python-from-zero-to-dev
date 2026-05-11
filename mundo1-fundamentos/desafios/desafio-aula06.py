# Desafio 1
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele. 
elemento_digitado = input("Digite algo: ")
print(f'O elemento {elemento_digitado} que você digitou é do tipo' , type(elemento_digitado))
print('Só tem espaços?', elemento_digitado.isspace())
print('É um número?', elemento_digitado.isnumeric() )
print('É alfabético?', elemento_digitado.isalpha())
print('É alfanumérico?', elemento_digitado.isalnum())
print('Está em letra maiúscula?', elemento_digitado.isupper())
print('Está em letra minúscula?', elemento_digitado.islower())
print('Está capitalizada?', elemento_digitado.istitle())