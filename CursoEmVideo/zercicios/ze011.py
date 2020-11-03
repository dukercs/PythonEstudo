altura = float(input('Entre com a altura da parede em metros: '))
largura = float(input('Entre com a largura da parede em metros:'))

tinta = 2
area = altura * largura

print('A área total é de {}m2 e você precisará de {} litros de tinta para pintá-la.'.format(area, area / 2))
