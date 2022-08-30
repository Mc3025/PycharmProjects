cont = ('zero','um','dois','três','quatro'
        ,'cinco','seis','sete','oito',
        'nove','dez','onze','doze','trese','quatorze',
        'quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
      num= int(input('Digite um numero de 0 a 20: '))
      if  0 <= num <= 20:
             break
      print('tente novamente', end=' ')
print(f'Você digitou o numero {cont[num]}')

