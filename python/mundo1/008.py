# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros!

m = float(input('Digitw uma distância em metros? '))

print('O valor em metros é: {:.0f}m'.format(m))
print('O valor em centimetros é: {:.0f}cm'.format(m*100))
print('O valor em milimetros é: {:.0f}mm'.format(m*1000))