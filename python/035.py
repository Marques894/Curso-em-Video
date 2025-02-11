# Descreva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triângulo.

print('-=' * 15)
print('Analisador de Triângulo.')
print('-=' * 15)

r1 = float(input('Digite o Primeiro seguimento: '))
r2 = float(input('Digite o Segundo seguimento: '))
r3 = float(input('Digite o Terceiro seguimento: '))
print('')

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('TEMOS UM TRIÂNGULO.')
else:
    print('NÃO TEMOS UM TRIÂNGULO')