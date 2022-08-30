soma = 0
media = 0
for c in range(1, 5):
    num = int(input('Digite o {}° valor: '.format(c)))
    soma +=num
    media = soma/4
if media >1:
    print('O valor é positivo')
else:
    print('O valor é negativo')
print('A soma entre os valores é {}'.format(soma))
print('A média entre os valores é {}'.format(media))
