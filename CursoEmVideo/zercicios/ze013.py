salario = float(input('Entre com valor bruto do salário do funcionário: '))
aumento = int(input('Entre com o percentual de aumento em %: '))

novosalario = salario + (salario * (aumento/100))

print('O novo salário será de R$ {:.2f}'.format(novosalario))