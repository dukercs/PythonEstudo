from datetime import date
print('-._ '*6)
print('CNN - Categorização')
print('-._ '*6)

ano = int(input('Atleta entre com seu ano de nascimento: '))
idade = date.today().year - ano

if idade <= 9:
    print('CATEGORIA: \033[34mMirim\033[m')
elif idade <= 14:
    print('CATEGORIA: \033[34mInfantil\033[m')
elif idade <= 19:
    print('CATEGORIA: \033[34mJúnior\033[m')
elif idade <= 25:
    print('CATEGORIA: \033[34mSênior\033[m')
else:
    print('CATEGORIA: \033[34mMaster\033[m')
