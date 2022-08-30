primeiro= int (input('Digite o primeiro termo : '))
razão= int(input('Digite a razão: '))
termo= primeiro
cont= 1
total= 0
mais = 10
while mais !=0:
     total= total + mais
     while cont <=total:
        print('{} - '.format(termo), end='')
        termo +=razão
        cont  += 1
     print(' Pausa ')
     mais= int(input('Quantos termos mais você quer mostrar: '))
print('fim')
print('O total de termos digitados foi {}'.format(total))



