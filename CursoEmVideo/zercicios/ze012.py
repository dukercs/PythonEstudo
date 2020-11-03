preco = float(input('Entre com o preço: '))
desconto = int(input('Entre com o desconto em %: '))

cobrar = preco - (preco * (desconto/100))

print('O valor com desconto é de {:.2f}!'.format(cobrar))