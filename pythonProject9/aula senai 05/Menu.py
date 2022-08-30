from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor : '))
opção= 0
while opção!=5:
    print('Escolha as opcõe seguintes:')
    print('''    [1] Somar
    [2] Multiplicar
    [3] Para saber o maior valor
    [4] Para digitar novos numeros 
    [5] Sair do programa ''')
    opção =int(input('Qual é a sua opção?   '))
    print('Finalizando o programa')
    if opção == 1:
        soma= n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opção==2 :
        produto= n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, produto))
    elif opção== 3:
        if   n1 > n2:
          maior= n1
        else:
             maior= n2
             print('O maior numero entre {} e {} é {}'.format(n1, n2,maior))
    elif opção ==4:
        n1=int(input('digite novamente o primeiro valor:'))
        n2=int(input('Digite novamente o segundo valor:'))
    elif opção== 5:
        sleep(2)
        print('Finalizando esta merda!!')