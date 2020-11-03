velocidade = float(input('Entre com a velocidade do carro: '))
if velocidade > 80.0:
    multa = (velocidade - 80.0) * 7.00
    print('\033[1;31m O carro foi multado trafegando em {} Km/h e para cada KM/h acima dos 80KM/h permitido será cobrado R$ 7,00 como multa\n'
          'Flagrado acima em {:.1f} Km/h e foi multado em R$ {:.2f}\033[m'.format(velocidade,(velocidade - 80), multa))
print('\033[1;32m Diriga com segurança!\033[m')