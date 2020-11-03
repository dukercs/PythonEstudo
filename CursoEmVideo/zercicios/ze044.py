print(' $ -'*6)
print('Vendas 2.0 - Simulador de preços')
print(' $ -'*6)


preco = float(input('Entre com o preço da etiqueta do produto em R$: '))
print('Veja as opções de pagamento:\n'
      '\033[1;32m[ 1 ]\033[m - À vista dinheiro/cheque - Desconto 10%\n'
      '\033[32m[ 2 ]\033[m - À vista no cartão - Desconto 5%\n'
      '\033[34m[ 3 ]\033[m - Em 2x no cartão - Preço de lista\n'
      '\033[31m[ 4 ]\033[m - Em 3x ou mais no cartão - 20% de juros')
pgto = int(input('Entre com a forma de pagamento escolhida: '))
parcelas = 0

if pgto != 0 and pgto < 5:
    if pgto == 1:
        pagar = preco - (preco * 0.1)
    elif pgto == 2:
        pagar = preco - (preco * 0.05)
    elif pgto == 3:
        pagar = preco
        parcelas = pagar / 2
    elif pgto == 4:
        pagar = preco + (preco * 0.2)
        financiamento = int(input('Entre com a quantidade de parcelas: '))
        if financiamento < 3:
            print('Use a opção 3')
        else:
            parcelas = pagar / financiamento

    if parcelas > 0:
        print('O valor total será de R$ {:.2f} e as parcelas serão de R$ {:.2f}'.format(pagar, parcelas))
    else:
        print('O valor total será de R$ {:.2f}.'.format(pagar))

else:
    print('OPÇÃO INVÁLIDA. Tente novamente!')

