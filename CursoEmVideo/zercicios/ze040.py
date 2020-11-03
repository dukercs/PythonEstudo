print('#'*20)
print('Calculo de aprovação')
print('#'*20)

nota1 = float(input('Entre com a nota 1: '))
nota2 = float(input('Entre com a nota 2: '))

media = float((nota2 + nota1) / 2)

print('Média: {:.1f}'.format(media))

if media < 5.0:
    print('\033[1;30;41mREPROVADO\033[m')
elif media >= 5.0 and media <= 6.9:
    print('\033[1;33mRECUPERAÇÃO\033[M')
else:
    print('\033[1;34mAPROVADO\033[m')
