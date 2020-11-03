numero = int(input("Digite um número: "))

print("1 - \033[1;31m Vermelho\033[m| 5 - \033[1;35m Rosa\033[m\n"
      "2 - \033[1;32m Verde\033[m   | 6 - \033[1;36m Ciano\033[m\n"
      "3 - \033[1;33m Amarelo\033[m | 7 - \033[1;37m Branco\033[m\n"
      "4 - \033[1;34m Azul\033[m    | 0 - Preto")
cor = 30 + int(input("Escolha a cor para a fonte da aplicação usando o número inteiro equivalente: \n"))

uni = numero // 1 % 10
dec = numero // 10 % 10
cen = numero // 100 % 10
mil = numero // 1000 % 10
print("A unidade é: \033[1;{0}m{1}\033[m".format(cor, uni))
print("A decimal é: \033[1;{0}m{1}\033[m".format(cor, dec))
print("A centena é: \033[1;{0}m{1}\033[m".format(cor, cen))
print("A milhar é: \033[1;{0}m{1}\033[m".format(cor, mil))