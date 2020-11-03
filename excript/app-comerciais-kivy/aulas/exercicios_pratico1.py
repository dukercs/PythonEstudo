"""
1) Faça um algoritmo que apenas imprima o seu nome na tela e em seguida finalize a aplicação.

2) Faça um algoritmo que solicite ao usuário digitar o seu nome e em seguida envie a seguinte frase para a
saída padrão: "O seu nome é: [nome do usuário]".

3) Faça um algoritmo que solicite o nome e a idade do usuário e então, envie a seguinte frase para o Console:
"O seu nome é <nome> e a sua idade é <idade>".

4) Faça um algoritmo que solicite ao usuário informar um número. Em seguida, armazene este número numa variável.
Por fim, envie esse número para a saída padrão.

5) Faça um algoritmo que solicite ao usuário informar um número. Em seguida, escreva a seguinte mensagem:
 "O número digitado foi: ".


"""

print("1) Faça um algoritmo que apenas imprima o seu nome na tela e em seguida finalize a aplicação.")
print("Rodolpho Costa Stach")

print()
print("2) Faça um algoritmo que solicite ao usuário digitar o seu nome e em seguida envie a seguinte frase para a saída padrão: O seu nome é: [nome do usuário].")
nome2 = input("Insira seu nome: ")
print("O seu nome é: ", nome2)

print()
print("3) Faça um algoritmo que solicite o nome e a idade do usuário e então, envie a seguinte frase para o Console: O seu nome é <nome> e a sua idade é <idade>.")
nome3 = input("Insira seu nome: ")
idade3 = int(input("Entre com a sua idade"))
print("O seu nome é ", nome3, "e a sua idade é ", idade3)

print()
print("4) Faça um algoritmo que solicite ao usuário informar um número. Em seguida, armazene este número numa variável. Por fim, envie esse número para a saída padrão.")
num4 = float(input("Entre com um número: "))
print(num4)

print()
print("5) Faça um algoritmo que solicite ao usuário informar um número. Em seguida, escreva a seguinte mensagem: O número digitado foi: .")
num5 = float(input("Entre com um número: "))
print("O número digitado foi %.2f" %num5)
