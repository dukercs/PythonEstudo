print('(.) '*7)
print('Calculo do IMV e avaliação')
print('(.) '*7)

peso = float(input('Entre com seu peso atual em Kg: '))
altura = float(input('Entre com a sua altura atual em metros: '))

imc = peso / (altura**2)

if imc <= 18.5:
    print('Seu IMC é {:.2f} e você está abaixo do peso.'.format(imc))
elif imc > 18.5 and imc <= 25:
    print('Seu IMC é {:.2f} e você está no peso ideal.'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu IMC é {:.2f} e você está de sobrepeso.'.format(imc))
elif imc > 30 and imc <=40:
    print('Seu IMC é {:.2f} e vocẽ está com obesidade.'.format(imc))
else:
    print('Seu IMC é {:.2f} e você está com obesidade mórbida procure um médico'.format(imc))