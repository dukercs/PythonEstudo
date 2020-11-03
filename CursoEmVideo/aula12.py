nome = str(input('Qual é o seu nome?\n'))

if nome == 'Rodolpho':
    print('Que nome bonito!')
elif nome == 'Katarina' or nome == 'Rafaela':
    print('Lindo nome, bem vinda família!')
else:
    print('Seu nome é bem normal')

print('Tenha um bom dia {}'.format(nome))
