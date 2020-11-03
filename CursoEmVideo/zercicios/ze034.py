salario = float(input('Entre com o salário: '))

if salario >= 1250.00:
    aumento = 10
else:
    aumento = 15
novo = salario + (salario * (aumento / 100))

print('Para um salário de R$ {:.2f} o aumento será de {}% e o novo salário será de R$ {:.2f}'.format(salario, aumento, novo))