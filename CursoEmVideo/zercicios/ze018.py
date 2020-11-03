from math import sin,cos,tan,radians
angulo = float(input('Entre com o angulo: '))
radiano = radians(angulo)
seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

print('Valores trigonométricos de seno, cosseno e tangente para o angulo {0:.2f}\nSeno: {1:.2f}\nCosseno: {2:.2f}\nTangente: {3:.2f}'.format(angulo, seno, cosseno, tangente))