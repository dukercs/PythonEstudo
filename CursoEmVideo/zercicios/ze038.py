print('*'*25)
print('     Compara valores')
print('*'*25)

num1 = float(input('Entre com o primeiro valor: '))
num2 = float(input('Entre com o segundo valor: '))

if num1 > num2:
    print('O \033[33mprimeiro\033[m valor é \033[34mmaior\033[m')
    print('O \033[33msegundo\033[m valor é \033[34mmenor\033[m')
elif num2 > num1:
    print('O \033[33msegundo\033[m valor é \033[34mmaior\033[m')
    print('O \033[33mprimeiro\033[m valor é \033[34mmenor\033[m')
elif num1 == num2:
    print('\033[33mNão existe\033[m valor maior, os dois são \033[34miguais\033[m')