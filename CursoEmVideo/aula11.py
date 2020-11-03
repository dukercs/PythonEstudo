'''print('\033[0;30;41mTeste\033[m')
print('\033[4;33;44mTeste\033[m')
print('\033[1;35;43mTeste\033[m')
print('\033[30;42mTeste\033[m')
print('\033[mTeste\033[m')
print('\033[7mTeste\033[m')'''

cores = {'limpa':'\033[m',
         'red':'\033[1;31m',
         'amarelo':'\033[1,33'}


nome = str('Rodolpho')
print('Olá {}{}{}! Muito prazer em te conhecer!'.format(cores['red'], nome, cores['limpa']))
