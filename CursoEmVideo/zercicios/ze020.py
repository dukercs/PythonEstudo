from random import shuffle

aluno = []
aluno.append(str(input('Entre com o nome do aluno 1:\n')))
aluno.append(str(input('Entre com o nome do aluno 2:\n')))
aluno.append(str(input('Entre com o nome do aluno 3:\n')))
aluno.append(str(input('Entre com o nome do aluno 4:\n')))

lista = list(aluno)
shuffle(lista)

print('A ordem de apresentação será: {}'.format(lista))