nota1 = float(input('Qual a primeira nota: '))
nota2 = float(input('Qual a segunda nota: '))
media = (nota1 + nota2)/2

print('A sua média foi {}.'.format(media))

if media >= 6.0:
    print('Sua média está acima da média desejada. Parabéns!')
else:
    print('Sua média foi abaixo do desejado, estude mais! ')