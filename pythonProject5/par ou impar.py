from random import randint
v= 0
while True:
    jogador = int(input('Digite um numero: '))
    computador = randint(0, 10)
    total = jogador + computador
    opção=' '
    while opção not in 'PI':
        opção = str(input('Voçê escolhe par ou impar? [P/I] ')).strip().upper()[0]
    print(f'voce jogou {jogador} e o computador jogou {computador} o total é {total}')
    if opção == 'P':
       if total % 2 == 0:
            print('Você venceu!')
            v+=1
       else:
            print('Você perdeu!')
            break
    elif opção in 'I':
       if total % 2 == 1:
           print('Você venceu!')
           v+=1
       else:
           print('Você perdeu !')
           break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Voce venceu {v} vezes')




