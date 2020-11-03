num1 = int(input('Entre com o num1: '))
num2 = int(input('Entre com o num2: '))
num3 = int(input('Entre com o num3: '))

lista = [num1, num2, num3]
lista.sort()

print('LISTA: O maior é: {} - O menor é: {}'.format(lista[-1], lista[0]))

if num1 > num2:
    if num1 > num3:
        maior = num1
    else:
        maior = num3
else:
    if num2 > num3:
        maior = num2
    else:
        maior = num3
if num1 < num2:
    if num1 < num3:
        menor = num1
    else:
        menor = num3
else:
    if num2 < num3:
        menor = num2
    else:
        menor = num3

print('CONDICAO: Maior: {}. - Menor: {}'.format(maior, menor))