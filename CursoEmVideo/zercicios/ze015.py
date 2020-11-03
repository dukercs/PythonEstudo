km = float(input('Entre com a quantidade de KM percorridos: '))
dias = int(input('Entre com a quantidade de dias que foi alugado: '))

preco = (0.15 * km) + (60.00 * dias)

print('O valor do aluguel foi de R$ {:.2f}!'.format(preco))