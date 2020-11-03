nome = str(input("Qual é o seu nome completo?\n")).strip().title()

nomearray = nome.split()

print('Primeiro nome: {}'.format(nomearray[0]))
print('Último nome: {}'.format(nomearray[-1]))