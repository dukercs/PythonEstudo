# coding=UTF-8
# Fatiamento
frase = 'Curso em Vídeo Python'

print("A partir da posição 9 até o final pulando de 3 em 3: ", frase[9::3])
print("O terceiro caractere a partir do final: ", frase[-3])



# Analise
print("Quantidade de caracteres com espaço - tamanho do array: ",len(frase))
print("Conta quantas letras o minúsculos tem na frase da posição 0 até 13:",frase.count('o',0,13))
print("Procura deo na frase e fala o onde foi encontrado no array: ",frase.find('deo'))
print("Procura Android na frase e fala onde foi encontrado, retorna -1 se não for encontrado: ",frase.find('Android'))
print("Existe Curso na frase?\n",'Curso' in frase)

# Transformacao
print("Troca Python por Android na frase: ",frase.replace('Python','Android'))
print("Frase em maiúsculo: ",frase.upper())
print("Frase em minúsculo: ",frase.lower())
print("Frase apenas com a primeira letra em maiúsculo: ",frase.capitalize())
print("Frase com as palavras separadas por espaço iniciam com letra maiúscula: ",frase.title())
print("Remove espaços em branco da direita: ",frase.rstrip())
print("Remove espaços em branco da esquerda: ",frase.lstrip())
print("Remove espaços em branco da esquerda e direita",frase.strip())

# Divisão
frasearray = frase.split()
print("Aqui dividimos a frase em um array (usando os espaços em branco) e vamos mostrar a segunda palavra: ",frasearray[3])


# Junção
print("Aqui vamos juntar o array criado com - (hífen): ",'-'.join(frasearray))


print("Toda a frase pulando de 2 em 2 caracteres: ",frase[::2])



print("Transforma toda a frase em maiúscula e conta quantas letras O: ",frase.upper().count('O'))

print("Pegua o array da frase e mostra o quarto caractere da terceira palavra: ",frasearray[2][3])


nome = input("Qual é o seu nome?\n")

print("Nome em maiúscula: ",nome.upper())
print("Nome em minúscula: ",nome.lower())
print("Quantidade de letras (sem espaços): ",len(nome.replace(' ','')))
nomearray = nome.split()
print("Quantidade de letras do primeiro nome: ",len(nomearray [0]))

numero = int(input("Digite um número: "))
uni = numero // 1 % 10
dec = numero // 10 % 10
cen = numero // 100 % 10
mil = numero // 1000 % 10
print("A unidade é: %i" %uni)
print("A decimal é: %i" %dec)
print("A centena é: %i" %cen)
print("A milhar é: %i" %mil)

cidade = input("Qual o nome da sua cidade?\n")
cidarray = cidade.split()
if cidarray[0].upper() == 'SANTO':
    print("Sim, sua cidade começa com Santo")
else:
    print("Não, sua cidade não começa com Santo")

if 'SILVA' in nome.upper():
    print("Você tem Silva no nome")
else:
    print("Você não é da família Silva")
