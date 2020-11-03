from random import randint
from time import sleep

print('--='*36)
print('Vamos brincar de adivinhação! Em qual número estou pensando ?')
print('--='*36)
num = int(input('Em um universo inteiro de 1 a 5 em qual número estou pensando? '))
print('PROCESSANDO...')
sleep(2)

computador = randint(1, 5)

if num == computador:
    print('Parabéns você acertou! Não espalhe')
else:
    print('Ainda não foi dessa vez! Tente de novo')
    print('Pensei no número {}!'.format(computador))