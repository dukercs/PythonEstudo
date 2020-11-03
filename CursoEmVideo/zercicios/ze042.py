print('/\\'*12)
print('Analisador de triângulos')
print('/\\'*12)
print('')
ab = float(input('Entre com o lado AB do triângulo: '))
bc = float(input('Entre com o lado BC do triângulo: '))
ca = float(input('Entre com o lado CA do triângulo: '))

if ab < bc + ca and bc < ab + ca and ca < ab + bc:
    print('Com os lados ab {0}, bc {1}, e ca {2} é possível fazer um triângulo, '.format(ab, bc, ca), end='')
    if ab == bc and bc == ca and ca == ab:
        print('\033[1;32mEquilátero\033[m')
    elif ab == bc or bc == ca or ca == ab:
        print('\033[1;32mIsósceles\033[m')
    elif ab != bc and bc != ca and ca != ab:
        print('\033[1;32mEscaleno\033[m')
else:
    print('Com os lados ab {0}, bc {1}, e ca {2} \033[1;31mnão\033[m é possível fazer um triângulo!'.format(ab, bc, ca))
