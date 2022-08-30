from random import randint
computador = randint(1,10)
print('Vamos ver se voce consegue adivinha os numeros que estou adivinhando')
print('Qual o seu palpite?')
acertou = False
palpite =0
while not acertou:
    jogador = int(input('Qual o seu palpite: '))
    palpite +=1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos... tente mais uma vez')
        elif jogador < computador:
            print('Mais... tente mais uma Vez ')
print('Voce acertou com {} tentativas. PARABENS!!'.format(palpite))

