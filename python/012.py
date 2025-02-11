# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto!

preco =  float(input('Qual o preço do priduto ?'))
desconto = preco*5/100

print('O valor do produto é R${:.2f}, com o desconto ele passa valer R${:.2f}'.format(preco, preco-desconto))