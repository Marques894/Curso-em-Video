# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date

ano = int(input('Qual ano gostaria de analisar ? Caso queira analisar o ano atual digite 0!'))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))