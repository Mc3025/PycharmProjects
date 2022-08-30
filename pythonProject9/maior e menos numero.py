resp = 'S'
soma = 0
count = 0
media = 0
maior= 0
menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma  += num
    count += 1
    if count ==1:
        maior= menor = num
    else:
        if num > maior:
            maior= num
        if num< menor:
            menor = num
    resp =str(input('Voce deseja continuar [S/N] ')).upper().strip()[0]
print('fim)')
media= soma /count
print('A soma dos numeros digitados é {} e sua média é {}'.format(soma, media ))
print('O maior numero é {}'.format(maior))
print('O numero {} é o menor numemro'.format(menor))
