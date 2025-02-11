# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.

# Exemplo: Ana Maria de Souza 
# Primeiro: Ana
# Segundo: Souza

n = str(input('Digite seu nome completo: ')).strip()
# O 'strip()' remove todos os espaços do começo e do final!

nome = n.split()
# O 'split()' Fatia os nome!
# exemplo: 'Renan' 'Marques'

print('O seu primeiro nome é: {}'.format(nome[0]))
print('O seu último nome é: {}'.format(nome[len(nome)-1]))

# Nome[len(nome)-1] irá acessar apenas um caractere da string.