sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo=str(input('Ficou louco digite novamente seu sexo:'))
print('Muito bem seu Sexo é {}'.format(sexo))
