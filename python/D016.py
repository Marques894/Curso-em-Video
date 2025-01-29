# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.

# Ex: Digite o numero 6.127
#     O numero 6.127 tem a parte inteira 6.

import math
num = float(input('Digite um numero:'))
print ('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))

# O 'trunc' arredonda um valor flutuante.
# Ex: Se voce digitar 4.44, ele vai me retornar 4.

# Tambem podemos fazer de outra forma...

from math import trunc
number = float(input('Digite outro valor:'))
print('O valor digitado foi {} e sua porção inteira é {}'. format(number, trunc(number)))

# Podemos analisar que são duas formar diferentes de fazer a mesma coisa.