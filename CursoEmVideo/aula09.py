# coding=UTF-8
# Fatiamento
frase = 'Curso em Vídeo Python'

print("1 - \033[1;31m Vermelho\033[m| 5 - \033[1;35m Rosa\033[m\n"
      "2 - \033[1;32m Verde\033[m   | 6 - \033[1;36m Ciano\033[m\n"
      "3 - \033[1;33m Amarelo\033[m | 7 - \033[1;37 Branco\033[m\n"
      "4 - \033[1;34m Azul\033[m    | 0 - Preto")
cor = 30 + int(input("Escolha a cor para a fonte da aplicação usando o número inteiro equivalente: \n"))

print("A partir da posição 9 até o final pulando de 3 em 3: \033[1;{0}m{1}\033[m".format(cor, frase[9::3]))
print("O terceiro caractere a partir do final: \033[1;{0}m{1}\033[m".format(cor, frase[-3]))

# Analise
print("Quantidade de caracteres com espaço - tamanho do array: \033[1;{0}m\033[1;{0}m{1}\033[m\033[m".format(cor, len(
    frase)))
print(
    "Conta quantas letras o minúsculos tem na frase da posição 0 até 13: \033[1;{0}m\033[1;{0}m{1}\033[m\033[m".format(
        cor, frase.count('o', 0, 13)))
print("Procura deo na frase e fala o onde foi encontrado no array: \033[1;{0}m{1}\033[m".format(cor, frase.find('deo')))
print(
    "Procura Android na frase e fala onde foi encontrado, retorna -1 se não for encontrado: \033[1;{0}m{1}\033[m".format(
        cor, frase.find('Android')))
print("Existe Curso na frase?\n\033[1;{0}m{1}\033[m".format(cor, 'Curso' in frase))

# Transformacao
print("Troca Python por Android na frase: \033[1;{0}m{1}\033[m".format(cor, frase.replace('Python', 'Android')))
print("Frase em maiúsculo: \033[1;{0}m{1}\033[m".format(cor, frase.upper()))
print("Frase em minúsculo: \033[1;{0}m{1}\033[m".format(cor, frase.lower()))
print("Frase apenas com a primeira letra em maiúsculo: \033[1;{0}m{1}\033[m".format(cor, frase.capitalize()))
print("Frase com as palavras separadas por espaço iniciam com letra maiúscula: \033[1;{0}m{1}\033[m".format(cor, frase.title()))
print("Remove espaços em branco da direita: \033[1;{0}m{1}\033[m".format(cor, frase.rstrip()))
print("Remove espaços em branco da esquerda: \033[1;{0}m{1}\033[m".format(cor, frase.lstrip()))
print("Remove espaços em branco da esquerda e direita \033[1;{0}m{1}\033[m".format(cor, frase.strip()))

# Divisão
frasearray = frase.split()
print("Aqui dividimos a frase em um array (usando os espaços em branco) e vamos mostrar a segunda palavra: ",
      frasearray[3])

# Junção
print("Aqui vamos juntar o array criado com - (hífen): \033[1;{0}m{1}\033[m".format(cor, '-'.join(frasearray)))

print("Toda a frase pulando de 2 em 2 caracteres: \033[1;{0}m{1}\033[m".format(cor, frase[::2]))

print("Transforma toda a frase em maiúscula e conta quantas letras O: \033[1;{0}m{1}\033[m".format(cor, frase.upper().count('O')))

print("Pegua o array da frase e mostra o quarto caractere da terceira palavra: \033[1;{0}m{1}\033[m".format(cor, frasearray[2][3]))
