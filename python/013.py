# Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% aumento!

salario = float(input('Qual o valario do funcionario ? '))
desconto = salario*15/100

print('Salario funcionario: R${:.2f}'.format(salario))
print('Salario funcionario com o desconto: R${:.2f}'.format(salario-desconto))