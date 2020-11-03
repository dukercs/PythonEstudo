# coding: utf8

print('Leia algo na tela e mostre o seu tipo primitivo e todas as informações possíveis sobre ele')

valor = input('Entre com qualquer informação: ')

print('Tipo primitivo', type(valor))
print('É possível converter para numérico?', valor.isnumeric())
print('É valor alfabético?', valor.isalpha())
print('É um valor alfanumérico?', valor.isalnum())
print('É um valor imprimível?', valor.isprintable())
print('É um valor decimal?', valor.isdecimal())
print('É um identificador?', valor.isidentifier())
print('Está em maiúsculo?', valor.isupper())
print('Está em minúsculo?', valor.islower())
print('É dígito?', valor.isdigit())
print('É um espaço?', valor.isspace())
print('É uma string capitalizada como título?', valor.istitle())

