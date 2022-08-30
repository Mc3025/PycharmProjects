clasbra=( 'Palmeiras','Athletico-PR','Atlético-MG','Corinthians','Internacional','Fluminense',
        'São Paulo','Flamengo','Botafogo','Santos','Avaí','Coritiba','América-MG','Bragantino','Ceará','Atlético-GO',
        'Goiás','Cuiaba','Juventude','Fortaleza')

print(f'Classificação do Brasileirão {clasbra}')
print('=-'*20)
print(f'O cinco primeiros colocados são:{clasbra[0:5]}')
print('=-'*20)
print(f'Os quatro ultimos colocados são: {clasbra[16:20]}')
print('=-'*20)
print(f'A ordem alfabetica dos times são{sorted(clasbra)}')
print('=-'*20)
print(f'O corinthians esta na {clasbra.index("Corinthians")+1} posição')