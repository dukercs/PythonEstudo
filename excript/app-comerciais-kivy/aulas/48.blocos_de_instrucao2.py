# coding: utf-8


'''

Váriaveis declaradas dentro de um bloco de instrução só são acessíveis de dentro deste bloco

if(true):
    var1=40
    print(var1)
<saída> 40

Uma variável declarada antes do bloco de instrução pode ser acessada de fora do bloco e o bloco pode alterar seu conteúdo

var2=100
if(True):
    var2=140
print(var2)
<saída> 140


'''


a = 25
if(True):
    a = 50
    if(False):
        b = 50
    a = 40