# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quanto dólares ela pode comprar!

# Considere 
# US$1,00=R$3,27

real = float(input('Quanto dinheiro voce tem na carteira ? '))
dolar = real/5.94

print('Com R${:.2f} voce possui US${:.2f}'.format(real,dolar))