numeros=[]
while True:
    n= int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Numero Adicionado com sucesso')
    else:
        print('O numero ja foi adicionado, não vou adicionar')
    r=str(input('Deseja continuar? [S/N]'))
    if r in 'Nn':
        break
print('-='*30)
numeros.sort()
print(f'Os numeros adicionados foram {numeros}')
