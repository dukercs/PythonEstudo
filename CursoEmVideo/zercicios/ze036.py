from time import sleep
print('\033[1;32m$\033[m.'*25)
print('\033[1;34m       Analisador de crédito imobiliário\033[m')
print('\033[1;32m$\033[m.'*25)

print('Limitação não comprometer mais que \033[1;31m30%\033[m da sua renda mensal.')

casa = float(input('Entre com o valor da casa em R$: '))
prazo = int(input('Prazo para pagamento em anos: '))
salário = float(input('Entre com seu salário bruto mensal em R$: '))
prestacoes = casa / (prazo * 12)

print('Imóvel: \033[1;32m{:.2f}\033[m\nPrestações: \033[1;32m{:.2f}\033[m\nRenda: \033[1;32m{:.2f}\033[m'.format(casa, prestacoes, salário))
print('Analisando')
sleep(1)
limite = salário * 0.3

if prestacoes > limite:
    print('Financiamento \033[31mnegado\033[m o valor das prestações R$ {:.2f} superam os 30% da sua renda de R$ {:.2f}'.format(prestacoes, salário))
else:
    print('Financiamento \033[32maprovado\033[m em {} meses com valor de R$ {:.2f} para as prestações'.format(prazo*12, prestacoes))