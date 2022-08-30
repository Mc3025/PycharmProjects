count = ('zero','um','dois','tres', 'quatro', 'cinco', 'seis' ,'sete','oito', ' nove',' dez',
         'onze', 'doze', 'treze','quatorze', 'quinze', 'desesseis', 'desessete', 'desoito',
         'desenove', 'vinte')
resp =' '
while True:
    num = int(input('Digite um valor de 0 a 20: '))
    if 0 <= num <= 20:
        break
    resp = str(input('Deseja continuar [S/N] : ')).strip().upper()[0]
    while resp not in 'SN':
        if resp == 'N':
            break
print(f'O numero que voce digitou por extenso é {count[num]}')