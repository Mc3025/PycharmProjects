numero = int(input('Dgite o numero 999 para parar: '))
cont=0
while numero != 999:
      numero = int(input('Digite o numero 999 para parar: '))
      if numero!= 999:
         cont +=numero
         total= numero + cont

print('A soma dos valores digitados é {}'.format(total))
