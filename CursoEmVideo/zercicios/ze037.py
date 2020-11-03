import emoji

print('0.1.\033[31mB\033[m.' * 5)
print('    \033[7mConversor de unidades\033[m')
print('0.1.\033[31mB\033[m.' * 5)

num = int(input(emoji.emojize('Entre com um número para convertê-lo :church: : ', use_aliases=True)))

conversao = int(input('Para qual base deseja convertê-lo? \n[ 1 ] - Binário\n[ 2 ] - Octal\n[ 3 ] - Hexadecimal\n'))

cores = {'azul': '\033[1;34m',
         'vermelho': '\033[1;31m',
         'amarelo': '\033[1;33m',
         'inverte': '\033[7;30m',
         'limpa': '\033[m'}

if conversao == 1:
    print('O número {0}{1}{2} em binário {3}{4:b}{5}'.format(cores['inverte'], num, cores['limpa'], cores['azul'], num,
                                                             cores['limpa']))
elif conversao == 2:
    print('O número {0}{1}{2} em Octal {3}{4:o}{5}'.format(cores['inverte'], num, cores['limpa'], cores['amarelo'],
                                                         num, cores['limpa']))
elif conversao == 3:
    print('O número {0}{1}{2} em Hexadecimal {3}{4:X}{5}'.format(cores['inverte'], num, cores['limpa'], cores['vermelho'],
                                                               num, cores['limpa']))
