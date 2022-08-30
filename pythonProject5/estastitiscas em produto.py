soma = 0
tot1000=0
menor = 0
cont= 0
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço :R$'))
    resp = ' '
    cont+=1
    soma += preço
    if preço >=1000:
        tot1000 +=1
    if cont == 1:
        menor= preço
    else:
        if preço < menor:
            menor= preço
    while resp not in 'SN':
        resp = str(input('Deseja continuar ? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'O valor total é de R${soma}')
print(f'Você tem {tot1000} produtos de com valor maior que R$1000.00')
print(f'O produto produto mais barato custa R${menor}')
