import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz quadrada de {num} é {math.ceil(raiz)}')


y = 15.67
print(math.trunc(y))
print(math.floor(y))
print(math.ceil(y))

# Caso eu quisesse importar somente uma função:
from math import trunc
from math import floor, sqrt # Importo mais de uma função da biblioteca

print(trunc(y))

import random
num = random.randint(1,10)
print(num)

