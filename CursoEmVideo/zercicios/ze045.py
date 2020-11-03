from emoji import emojize
from random import randint
from time import sleep

def emo(num):
    if num == 1:
        return emojize('\033[31m:fist:\033[m', use_aliases=True)
    elif num == 2:
        return emojize(':hand:', use_aliases=True)
    elif num == 3:
        return emojize('\033[1;32m:v:\033[m', use_aliases=True)

print(emojize(' {}  {}  {} '.format(emo(1), emo(2), emo(3)), use_aliases=True)*5)
print('            JOGO DE JOKENPÔ')
print(emojize(' {}  {}  {} '.format(emo(1), emo(2), emo(3)), use_aliases=True)*5)

print(emojize('Escolha entre:\n1-Pedra: {}\n2-Papel {}\n3-Tesoura {}\n0-Sair'.format(emo(1), emo(2), emo(3), use_aliases=True)))
pessoa = int(input('Entre com sua escolha: '))
computador = randint(1,3)

if pessoa != 0 and pessoa < 4:
    print('JO KEN PÔ')
    for x in range(1, 3):
        print(emo(1), end='')
        sleep(.5)
        print(' {} '.format(emo(2)), end='')
        sleep(.5)
        print(emo(3))
        sleep(.8)

    if pessoa == computador:
        print('Pessoa {} - Computador {}'.format(emo(pessoa), emo(computador)))
        print('Empate')
    elif pessoa == 3 and computador == 1:
        print('Pessoa {} - Computador {}'.format(emo(pessoa), emo(computador)))
        print('Venci!')
    elif computador == 3 and pessoa == 1:
        print('Pessoa {} - Computador {}'.format(emo(pessoa), emo(computador)))
        print('Parabéns você venceu!')
    elif pessoa > computador:
        print('Pessoa {} - Computador {}'.format(emo(pessoa), emo(computador)))
        print('Parabéns você venceu!')
    elif computador > pessoa:
        print('Pessoa {} - Computador {}'.format(emo(pessoa), emo(computador)))
        print('Venci!')
else:
    print('Saindo...')


