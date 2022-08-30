listagen=('whey',56.00,
          'creatina', 50.60,
          'malto', 20.00,
          'abulmina', 60.00,
          'dextroze', 45.95,
          'hipercalorico', 71.00)
for pos in range(0,len(listagen)):
    if pos % 2==0:
        print(f'{listagen[pos]:.<30}', end='')
    else:
        print(f'R${listagen[pos]:.>7.2f}')
