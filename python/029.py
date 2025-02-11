# Escreva um programa que leia a velocidade e um carro.
# Se ele ultrapassar 80km/h, mostrar uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00, por km acima do limite.

velocidade = float(input('Qual é a velocidade atual do carro ? '))

if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('Você tomou uma multa no valor de {:.2f}!'.format(multa)) 

print('Tenha um bom dia! Dirija com segurança!')
