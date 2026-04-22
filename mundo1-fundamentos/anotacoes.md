# Anotações Gerais

. Aula04

- No python para delimitar as mensagens de dois modos, com aspas simples '' ou aspas duplas "", mas a grande maioria dos programadores utilizam as aspas simples.
  Ex: print('Hello World')

- Comando para concatenar textos: print('exemplo1'+'exemplo2') = exemplo1exemplo2
  Podemos fazer isso com o "+"(Quando tiver apenas textos) ou com a ","(Quando tiver números e textos por exemplo, diferentes tipos de variáveis), existem casos que um é melhor e que outro é melhor.

. Aula05

- Tipos de variáveis primitivas e Saídas de Dados:
int: Números interios, exemplo: 7, -4, 0, 9875
float: Número flutuantes, exemplo: 4.5, 0.076, -15.223, 7.0 (Obs: em python a vírgula das casas decimais são representadas por ".")
bool: Valor de verdaeiro ou falso, exemplo: True e False (Obs: Sempre começa com letra maiúscula, True = 1 e False = 0)
str: Conjunto de carcteres, exemplo: 'Olá', '7.5', ''

- Método type(variável): é um método em que ele fala o tipo da variável que foi inserida nele.
Ex: 
ex = "Nome"
print(type(ex))
saída: <class 'str'>

- Método variável.isnumeric(): Método que retorna se a variável é numérica com True ou se não é, com False. (Obs: só é possível se colocar apenas o input sem converter para nenhum tipo específico)

- Método variavel.isalpha(): Método que retorna True ou False se a variável é letra ou não. 

- Método variavel.isalnum(): Método que retorna True ou False se a variável tem letra ou número. (Obs: existem diversos métodos is)
