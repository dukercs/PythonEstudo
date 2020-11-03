distancia = float(input('Entre com a distância da viagem em KM: '))

'''if distancia >= 200:
    km = 0.45
    preco = distancia * km
else:
    km = 0.50
    preco = distancia * km'''

km = 0.50 if distancia <= 200 else 0.45
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45


print('O valor cobrado será de R$ {:.2f} por KM e o valor total será de {:.2f}.'.format(km, preco))