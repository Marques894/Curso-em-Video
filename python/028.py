# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuario venceu ou perdeu.

from random import randint
from time import sleep

comput = randint(0,5)

print('-=-' * 20)
print('Vou pensar de um numero de 0 a 5. Tente advinhar')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei ? '))
print('Processando...')
sleep(3)

if jogador == comput:
    print('Parabéns! Você venceu! Número:{}'.format(jogador));
else:
    print('Ganhei! Eu pensei no numero {} e você colocou o numero {} !'.format(comput, jogador))