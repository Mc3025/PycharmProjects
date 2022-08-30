km = float(input('Digite quantos quilometros foram percorridos: '))
dia = float(input('O carro foi alugado por quantos dias?  '))
diaria = 60.00 * dia
kmrodado = 0.15 * km
total = diaria + kmrodado
print('O valor da diaria é {:.2f} e o valor por km rodado é {:.2f}'.format(diaria, kmrodado))
print('O valor total a ser pago é de {:.2f}'.format(total))
