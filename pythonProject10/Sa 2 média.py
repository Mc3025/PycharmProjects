soma = 0
cont = 0
maior = 0
menor = 0
for c in range(1,21):
  valor = int(input('Digite o {}° valor: '.format(c)))
  soma = soma + valor
  media = soma/20
  if c==1:
    maior = valor
    menor= valor
  else:
    if valor > maior:
      maior = valor
    if valor < menor:
        menor = valor
print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))
print ('A soma entre os valores digitados são {}'.format(soma))
print('A média entre os 20 valores é {}'.format(media))
