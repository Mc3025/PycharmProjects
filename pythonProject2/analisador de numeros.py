num= (int(input('digite um valor:')),
        int(input('digite um valor:')),
        int(input('digite um valor:')),
        int(input('digite um valor:')))
print(f' Voce digitou {num}')
print(f'O numero 9 aprece {num.count(9)} veses')
if 3 in num:
    print(f'O numero 3 aparece na {num.index(3)+1}° posição')
else:
    print('O numero 3 não aparece em nenhuma posição ')
print(f'Os numero pares digitados foram ', end='')
for n in num:
    if n % 2==0:
        print(n, end=' ')