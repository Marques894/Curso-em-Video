# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

km = float(input('Quantos km voce rodou com o carro ? '))
dias = int(input('Quantos dias o carro foi alugado ?'))
pkp = dias*60
pda = km*0.15
total = pda+pkp

print('='*15)
print('Preço kilometros percorridos: {}'.format(pda))
print('Preço por dias alugados: {}'.format(pkp))
print('Preço total a pagar: {}'.format(total))
print('='*15)