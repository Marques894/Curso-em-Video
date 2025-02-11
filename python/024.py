# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

# .srtrip() com essa tag resolvemos a questão dos espaços tanto no começo quanto no final da frase digitada, lembrando que espaços entre palavras não resolvemos!

cid = str(input('Em que cidade você nasceu ?')).strip()
print(cid[:5].upper() == 'SANTO')
