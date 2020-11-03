nome = str(input("Qual é o seu nome?\n")).strip()

print("1 - \033[1;31m Vermelho\033[m| 5 - \033[1;35m Rosa\033[m\n"
      "2 - \033[1;32m Verde\033[m   | 6 - \033[1;36m Ciano\033[m\n"
      "3 - \033[1;33m Amarelo\033[m | 7 - \033[1;37m Branco\033[m\n"
      "4 - \033[1;34m Azul\033[m    | 0 - Preto")
cor = 30 + int(input("Escolha a cor para a fonte da aplicação usando o número inteiro equivalente: \n"))

print("Nome em maiúscula: \033[1;{0}m{1}\033[m".format(cor, nome.upper()))
print("Nome em minúscula: \033[1;{0}m{1}\033[m".format(cor, nome.lower()))
print("Quantidade de letras (sem espaços): \033[1;{0}m{1}\033[m".format(cor, len(nome.replace(' ', ''))))
nomearray = nome.split()
print("Quantidade de letras do primeiro nome: \033[1;{0}m{1}\033[m".format(cor, len(nomearray[0])))