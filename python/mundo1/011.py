# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantodade de tinta nessesaria para pinta-la, sabendo que cada litro de tinta, pinta um area de 2m²!

lag = float(input('Qual a largura da parede ? Largura:'))
alt = float(input('Qual a altura da parede ? Altura:'))
area = lag*alt

print('Area: {:.2f}'.format(area))
print('Você vai precisar de {:.2f}L de tinta para essa parede de {:.2f}m²'.format(area/2, area))