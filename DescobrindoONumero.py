## 
#  DescobrindoONumero.py
#  
#  Copyright (c) 2020, Elieder Sousa
#  eliedersousa<at>gmail<dot>com
#  
#  Distributed under the MIT license.
#  
#  @date     18/09/20
#  
#  @brief       Este é um pequeno script que cria uma tabela para descobrir o número que a pessoa escolheu.
#               Aqui são usados conceitos aprendidos nas aulas de FCC.
#               Com programação, a brincadeira fica um pouco sem graça, por motivar a pessoa a achar que o PC tem memorizado todos os números.
#               Mas quando se descobre a lógica da brincadeira, podemos brincar com papel e caneta!
##


import random
import math

tabela = []
maximo = 5

def bitIsOn( num, bit ):
    if num >> bit & 1:
        return True
    else:
        return False
        
def numeroEscolhido( lista ):
    numero = 0
    for i in lista:
        if ( i > maximo or i < 1 ):
            return "ERRO, você informou um número de coluna inexistente!"
        numero += 2**(i-1)
    return numero

def printTabela( tabela ):
    print("╒" + ("═" * ( math.floor(math.log10(2**maximo) + 1) * maximo + maximo - 1) + "╕"))
    # Imprime os números das colunas
    numeroDasColunas = ""
    for i in reversed(range(1, maximo + 1)):
        numeroDasColunas += str(i).rjust( math.floor(math.log10(2**maximo) + 1) ) + "│"
    print("│" + numeroDasColunas + "<=== Número da coluna")
    print("╞" + ("═" * ( math.floor(math.log10(2**maximo) + 1) * maximo + maximo - 1) + "╡"))
    for linha in reversed(range(len(tabela[0]))):
        temp = ""
        for coluna in reversed(range(len(tabela))):
            temp += "│" + str(tabela[coluna][linha] ).rjust( math.floor(math.log10(2**maximo) + 1) )
        print( temp + "│")
    print("╘" + ("═" * ( math.floor(math.log10(2**maximo) + 1) * maximo + maximo - 1) + "╛"))
    
for deslocamento in range(0, maximo):
    tabela.append([])
    for numero in range(1, 2 ** maximo):
        if bitIsOn( numero, deslocamento ):
            tabela[deslocamento].append(numero)
    random.shuffle(tabela[deslocamento])

print("Vamos fazer uma brincadeira. Eu vou colocar alguns números dispostos em fileiras, e você escolhe um número de 1 a", (2**maximo - 1),".")
print("Depois de escolher o número, informa para mim em quais COLUNAS ele se encontra (não linhas hein!). Informe as colunas separadas por espaços. O número da coluna é aquela primeira linha que está escrito \"5 4 3 2 1\" .")
print("Exemplo: digamos que o número que você escolheu está nas colunas 1, 3, 4. Você vai digitar assim: 1 3 4")
print("Com um pouco de cálculo binário, eu posso dizer para você qual número escolheu! :D ")
printTabela( tabela )

while (True):
    col = [int(i) for i in input("Digite os números das colunas em que o número escolhido está: ").split(" ")]
    print("O número que você escolheu foi:", numeroEscolhido( col ) )
    