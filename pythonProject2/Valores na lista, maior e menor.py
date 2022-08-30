valores = []
for v in range(0,5):
     num=int(input(f'Digite o {v} valor:'))
     valores.append(num)
print(valores)
print(f'O maior valor digitado na lista foi {max(valores)} nas posicões ',end='')
for i, v in enumerate(valores):
    if v ==max(valores):
        print(f'{i}...',end='')
print (f'O menor valor digitado na lista é {min(valores)} nas posiçoes ',end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}...',end='')