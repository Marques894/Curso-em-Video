# Crie um programa que leia o nome de uma pessoae mostre: 
# -O nome com todas as letras maiúsculas 
# -O nome com todas as letras minusculas
# -Quantas letras tem ao todo sem considerar os espaços
# -Quantas letras tem o primeiro nome

nome = str(input('Digite o seu nome completo: ')).strip()

print('O nome com todas as letras maiúsculas: {}'.format(nome.upper()))

print('O nome com todas as letras minusculas: {}'.format(nome.lower()))

print('Quantas letras ao todo sem cosiderar os espaços: {}'.format(len(nome) - nome.count(' '))) 

#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
