from datetime import date
print('º'*37)
print('Valida tempo para alistamento militar')
print('º'*37)

atual = date.today().year
ano = int(input('Recruta qual é o seu ano de nascimento?\n'))
idade = atual - ano

if idade < 18:
    saldo = 18 - idade
    print('Recruta você deve se alistar em \033[32m{}\033[m anos'.format(saldo))
    print('Seu alistamento será em {}'.format(atual + saldo))
elif idade == 18:
    print('Recruta você deve se apresentar ainda neste ano')
elif idade > 18:
    saldo = idade - 18
    print('Recruta você já passou \033[1;31m{}\033[m anos do seu prazo de alistamento'.format(saldo))
    print('Seu ano de alistamento foi {}'.format(atual - saldo))
