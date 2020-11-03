from random import choice
aluno = []
aluno.append(str(input('Entre com o nome do aluno 1:\n')))
aluno.append(str(input('Entre com o nome do aluno 2:\n')))
aluno.append(str(input('Entre com o nome do aluno 3:\n')))
aluno.append(str(input('Entre com o nome do aluno 4:\n')))

print('O aluno sorteado foi {}!'.format(choice(aluno)))

