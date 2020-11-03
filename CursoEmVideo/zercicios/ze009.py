n1 = int(input('Entre com um número para sua tabuada: '))


multiplicador = 1
print('Tabuada do {}'.format(n1))
print('-'*15)
while multiplicador < 11:
    print('{0} x {1:2} = {2}'.format(n1, multiplicador, n1 * multiplicador))
    multiplicador = multiplicador + 1
print('-'*15)
