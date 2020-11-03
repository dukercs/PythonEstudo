# coding = utf8

# Ze1
print("Ver se o número é positivo, negativo ou zero")
num1=int(input("Digite um número: "))
if(num1 == 0):
    print("Número igual a zero")
else:
    if (num1 < 0):
        print("Número negativo")
    else:
        print("Número positivo")

# Ze2
print("Ver se o número é par ou impar")
par = num1 % 2
if(par == 0):
    print("O número é par!")
else:
    print("O Número é impar")

# Ze3
print("Leitura de dois números e ver qual é o maior")
num2=int(input("Entre com o segundo valor: "))
if(num1 > num2):
    print("O número maior é %i", num1)
else:
    print("O número maior é %i", num2)

# Ze4
print("Validar maior-idade!")
idade=int(input("Favor entre com sua idade: "))
if(idade<=0):
    print("A sua idade não poder 0 ou menor do que 0")
if(idade>=18):
    print("Você já é maior de idade. Vá pagar boletos!")
else:
    print("Você é menor de idade, não pode acessar!")

# Ze5
print("Ver idade da mãe ao nascer")
idadefilho = int(input("Entre com a idade do filho: "))
if(idadefilho<=0):
    print("A sua idade não poder 0 ou menor do que 0")
idademae = int(input("Entre com a idade da mãe: "))
if(idademae<=0 or idademae < idadefilho + 12):
    print("A idade da mae não pode ser 0, menor do que 0, menor que a idade do filho somado 12")
idadematerna = idadefilho - idademae
print("A idade da mãe quando o filho nasceu era: %i", idadematerna)

# Ze6
print("Imprima 50 vezes o caractere traço - sem usar loop")
char = "-"
char = char * 50
print(char)

# Ze7
print("Pede numero e imprime se é par ou ímpar")
num=int(input("Entre com um número: "))
resto = num % 2
if (resto == 0):
    print("Par")
else:
    print("Ímpar")

# Ze8
print("Comparar número maior e imprimir em ordem maior para menor: ")
num1=int(input("Entre com um número: "))
num2=int(input("Entre com outro número: "))
if(num1 > num2):
    ordem1=num1
else:
    ordem2=num2
print(ordem1+" "+ordem2)

# Ze9
print("Verificar se valor é número inteiro")
valor1=5
if type(valor1) == int:
    print("Inteiro")
else:
    print("O tipo de valor é: ", type(valor1))

# Ze10
print("Verificar se valor é String")
str1="Texto plano"
if type(str1) == str:
    print("String")
else:
    print("O tipo de valor é: ", type(valor1))

# Ze11
print("Verificar se valor é número decimal")
float1=5.5
if type(float1) == float:
    print("Ponto flutuante ou decimal")
else:
    print("O tipo de valor é: ", type(valor1))

# Ze 12
print("Entrada de valor numérico e verificar se o número é inteiro ou decimal")
entrada1 = input("Por favor entre com um valor numérico: ")
if type(entrada1) == int:
    print("Valor inteiro")
elif type(entrada1) == float:
    print("Valor decimal")
else:
    print('Entrada inválida do tipo: ', type(entrada1))

# Ze 13
print("Ler 3 numeros e imprima o maior deles")
num1 = float(input("Entre com o primeiro número: "))
num2 = float(input("Entre com o segundo número: "))
num3 = float(input("Entre com o terceiro número: "))
maior = 0
if num1 > num2:
    maior = num1
if num1 == num2:
    maior = num2
if num1 < num2:
    maior = num2
if maior == num3:
    print("Erro todos os numeros são iguais!!")
if maior < num3:
    maior = num3
print("O maior número é: %i", maior)

# Ze 14
print("Ler 3 numeros e imprima em ordem crescente")
num1 = float(input("Entre com o primeiro número: "))
num2 = float(input("Entre com o segundo número: "))
num3 = float(input("Entre com o terceiro número: "))
ord1 = 0
ord2 = 0
ord3 = 0

