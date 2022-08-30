from random import randint

numeros=(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(numeros)
for n in numeros:
    print(n)
print(f'o maior numero é {max(numeros)}')
print(f'O menor numero é {min(numeros)}')