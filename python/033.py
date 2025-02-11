# Faça um programa que leia três numeros e mostre qual é o MAIOR e qual é o MENOR.

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

menor = a 
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('')
print('O menor valor digitado foi {}'.format(menor))

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O maior valor digitado foi {}'.format(maior))
