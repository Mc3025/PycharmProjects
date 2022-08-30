total18 = 0
totalm=0
totalf=0
mulher20=0
while True:
    idade=int(input('Idade: '))
    sexo=' '
    resposta = ' '
    while sexo not in 'MF':
        sexo=str(input('Qual o Sexo? [M/F]')).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        totalm+=1
    if sexo == 'F' and idade >=20:
        totalf+=1

    while resposta not in 'SN':
        resposta= str(input('Deseja continuar?[S/N]')).strip().upper()[0]
    if resposta == 'N':
            break
print(f'O total de pessoas maiores de 18 anos cadastrados é de {total18}')
print(f'O total de homens cadastrados é de {totalm}')
print(f'O total de mulheres acima de 20 anos cadastrada é de {totalf} ')
