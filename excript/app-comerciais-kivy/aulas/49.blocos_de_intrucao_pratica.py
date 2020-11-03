# coding: utf-8

num1 = int(input("Digite um número: "))

if (num1 > 10):
    print("O valor e maior do que 10!")
    if (num1 <= 15):
        print("O valor é maior do que 10, mas menor do que 15")
    else:
        if (num1 <= 50):
            print("O valor é maior do que 10, mas menor do que 50!")
        else:
            print("O valor é maior do que 50")
else:
    if (num1 > 5):
        print("O número é menor do que 10 mas maior do que 5!")
        if (num1 == 7):
            print("o número é igual a 7!")
    else:
        print("O valor é menor do que 5.")
