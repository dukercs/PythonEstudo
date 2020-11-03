reais = float(input('Entre com quanto você possui em dinheiro: '))
cotacao = float(4.40)

print('Com o valor de R$ {:.2f} você consegue comprar US$ {:.2f} com a cotacao de {:.2f}.'.format(reais, reais / cotacao, cotacao))