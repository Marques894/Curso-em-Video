# Desenvolva um programa que pergunte a distância de uma viagem em km. Calculeo preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.

distancia = float(input('Digire a distancia da sua viagem: '))

if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
    
print('Voce vai pagar o valor de {:.2f}'.format(preço))