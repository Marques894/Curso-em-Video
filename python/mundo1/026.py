# Faça um programa que leia uma frase pelo teclado e mostre:

# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez 
# Em que posição ela aparece a ultima vez

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {}'.format(frase.count('A')))

# O 'strip()' remove todos os espaços do começo e do final!

# O '.upper()' passa todas as letras das frase para maiusculas. 

# O '.lower()' passa todas as letras das frase para minuscula. 

# Pois quando pedirmos para verifcar e mostrar na tela quantos 'A' ou 'a' contem dentro da frase ele consiga indentificar corretamente!

# A '(frase.count('A'))' verifica dentro da frase informada pelo usuario!

print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))

# A '(frase.find('A'))' verifica em qual posição esta a primeira letra A! 

# Podemos ver que ela começaria na posição 0, porem quando eu adicionei '+1' a letra A passou a estar na posição 1!

print('A ultima letra A apece na posição {}'.format(frase.rfind('A')+1))