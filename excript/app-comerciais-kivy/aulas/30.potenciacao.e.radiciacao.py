
# Potenciação o operador é **
print(9**3)

"""
Com esse operador podemos fazer a enésima raiz de qualquer número seguindo a seguinte lógica matemática

Um número elevado ao inverso de sua potência é a sua raíz
9^2 = 81

81 ^ (1/2) = 9  
"""

potencial = 81**9

raizes = 150094635296999121 ** (1/9)

print(potencial, raizes)


#Vamos brincar um pouco

base = float(input("Entre com o valor da base:"))
expoente = float(input("Entre com a potência:"))
print()

potencia = base ** expoente
raiz = potencia ** (1/expoente)

print("A", expoente, "potencia de", base, "é", potencia)

print("A", expoente, "raíz de", potencia, "é", raiz)






