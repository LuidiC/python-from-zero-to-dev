# Anotações Gerais

## Aula 04

- No python para delimitar as mensagens de dois modos, com aspas simples '' ou aspas duplas "", mas a grande maioria dos programadores utilizam as aspas simples.
  Ex: print('Hello World')

- Comando para concatenar textos: print('exemplo1'+'exemplo2') = exemplo1exemplo2
  Podemos fazer isso com o "+"(Quando tiver apenas textos) ou com a ","(Quando tiver números e textos por exemplo, diferentes tipos de variáveis), existem casos que um é melhor e que outro é melhor.

## Aula 05

- Tipos de variáveis primitivas e Saídas de Dados:
int: Números interios, exemplo: 7, -4, 0, 9875
float: Número flutuantes, exemplo: 4.5, 0.076, -15.223, 7.0 (Obs: em python a vírgula das casas decimais são representadas por ".")
bool: Valor de verdaeiro ou falso, exemplo: True e False (Obs: Sempre começa com letra maiúscula, True = 1 e False = 0)
str: Conjunto de carcteres, exemplo: 'Olá', '7.5', ''

- Método `type(variável)`: é um método em que ele fala o tipo da variável que foi inserida nele.
Ex: 
ex = "Nome"
print(type(ex))
saída: <class 'str'>

- Método `variável.isnumeric()`: Método que retorna se a variável é numérica com True ou se não é, com False. (Obs: só é possível se colocar apenas o input sem converter para nenhum tipo específico)

- Método `variavel.isalpha()`: Método que retorna True ou False se a variável é letra ou não. 

- Método `variavel.isalnum()`: Método que retorna True ou False se a variável tem letra ou número. (Obs: existem diversos métodos is)

## Aula 06 

- Método `variável.isspace()`: Método que retorna True ou False se a variável só contém espaçoes.

- Método `variável.isupper()`: Método que retorna True ou False se a variável está totalmente em letras maiúsculas.

- Método `variável.istitle()`: Método que retorna True ou False se a variável está capitalizada (Começa com letra maiúscula e o resto é minúsculo). 

- Método `variavel.strip()`: Método que retira todos os espaços vazios das variáveis
Ex: x = " exemplo"
x.strip()
x = "exemplo"

## Aula 07

Operadores 

{variavel:.numf}: difinui para o número para o número de casas que você determinar na parte do num.
end ='' : Não quebra a linha de um print para o outro. 
\n : Quebra a de elementos dentro de um mesmo print.

Operadores aritméticos 

+ -> adição
- -> subtração 
* -> multiplicação 
/ -> divisão 
** -> potência 
// -> divisão inteira 
% -> resto da divisão 
== -> é igual a?  

Ordens de execução/precedências 
1. () -> Utilizamos apenas elas em expressões aritméticas dentro do pyton, {} e [] são para outras coisas dentro da linguagem.  
2. ** 
3. *, /, //, % -> Resolve quem apareceu primeiro. 
4. +, -

Observação: É possível utilizar a função de potência `pow(num,num)` para realizar as potências entre o primeiro número elevado ao segundo, porém perdemos a ordem de execução quando a utilizamos. 

Dica: Para fazer raiz quandrada podemos fazer num ** (1/2), raiz cúbica num ** (1/3)

## Aula 08

Para incluir algo na linguagem de programação python é necessário colocar o comando `import` (bibliotecas por exemplo).
Ex:
- import bebidas: importa todas as bebidas para o meu projeto
- from bebidas import café: importa somente o café da biblioteca bebidas (economiza um pouco mais de memória) 

-> Bibliotecas interessantes:
. Math:
Bibliteca de funções matemáticas. 
`ceil`: Função que arredonda os números para cima. 
`floor`: Função que arredonda os números para baixo.
`trunc`: Truncar o número, eliminar da vírgula para frente.
`pow`: Fazer a potência de 2 números
`sqrt`: Fazer a raiz quadrada  
`factorial`: Calculo de fatorial de um número

Curiosidade: 
Se digitar `import` + Ctrl + SPACE, aparece todas as bibliotecas disponíveis para importar. 

## Aula 09

### Manipulação de cadeias de Texto: 

Toda a variável String é uma lista/array de caracteres.

nome = Luidi -> [L,u,i,d,i]
print(nome[3]) = d
print(nome[2-5]) = idi 
print(nome[0:4:2]) = Li
print(nome[:3]) = Lui
print(nome[1:]) = uidi

. Funções Importantes:
`len(frase)`: Função que mostra a quantidade de caracteres. 
`variavel.count('caracter a ser analisado')`: Função que mostra quantas vezes determinado caracter aparece na variavel.
`variavel.find('conjunto de caracteres')`: Função em que posição de caracter eu achei pela primeira vez o conjunto de caracteres. 
Obs: Caso receba o valor -1, siginifica que aquele conjunto de caracteres não existe na variavel. 
`Conjunto de caracteres in variavel`: Função que retorna True ou False se acahar ou não aquele conjunto na variável. 
`variavel.replace('XYZ', 'ABCDEF')`: Substitui o primeiro conjunto de carcateres pelo segundo. 