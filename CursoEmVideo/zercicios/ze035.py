print('/\\'*40)
print('Analisador de triângulos')
print('/\\'*40)
print('')
ab = float(input('Entre com o lado AB do triângulo: '))
bc = float(input('Entre com o lado BC do triângulo: '))
ca = float(input('Entre com o lado CA do triângulo: '))


if ab < bc + ca and bc < ab + ca and ca < ab + bc:
    print('Com os lados ab {0}, bc {1}, e ca {2} é possível fazer um triângulo!'.format(ab, bc, ca))
else:
    print('Com os lados ab {0}, bc {1}, e ca {2} \033[1;31mnão\033[m é possível fazer um triângulo!'.format(ab, bc, ca))
