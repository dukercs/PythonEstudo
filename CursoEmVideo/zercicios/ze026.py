frase = str(input("Digite uma frase:\n")).strip().upper()

print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A posição da primeira letra A foi {}'.format(frase.find('A')+1))
print('A posição da última ocorrência da letra A foi {}'.format(frase.rfind('A')+1))
