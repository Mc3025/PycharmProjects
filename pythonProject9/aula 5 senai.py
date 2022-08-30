preço = float(input('Digite o valor da mercadoria: R$ '))
desconto = (preço/100)*15
total= preço - desconto
print('O preço do produto é {:.2f}, o total do preço com 15% de desconto é {:.2f}'.format(preço, total))