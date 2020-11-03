from math import hypot

catetooposto = float(input('Entre com o valor do cateto oposto: '))
catetoadj = float(input('Entre com o valor do cateto adjacente: '))

#hipotenusa = ((catetooposto ** 2) + (catetoadj ** 2)) ** (1/2)
hipotenusa = hypot(catetooposto, catetoadj)

print('O valor da hipotenusa é de: {:.2f}'.format(hipotenusa))