## 
#  Representacao IEEE754.py
#  
#  Copyright (c) 2020, Elieder Sousa
#  eliedersousa<at>gmail<dot>com
#  
#  Distributed under the MIT license.
#  
#  @date     12/09/20
#  
#  @brief       Este é um tutorial da aula sobre a representação do número em ponto flutuante pela norma IEEE 754
#               Agradecimentos ao professor Israel pela paciência.
##  

import math

precisao = 10

# Retorna a representação do número em ponto flutuante pela norma IEEE 754
def i3e754 ( n ):
    # Precisao do ponto flutuante. 2^precisao
    binario = bin(math.floor( n * (2**precisao) ))[2:]
    return binario


def tutorial( n ):
    print("\n1) Transforme esse número em binário.")
    binario = i3e754( abs(n) )
    binarioComVirgula = binario[:(len(binario)-precisao)] + "," + binario[(len(binario)-precisao):]
    print( n, "=", binarioComVirgula )
    print("\n2) Normalize o número binário encontrado. Isto é feito 'andando' a vírgula N casas para a esquerda, a fim de fazer o número ter apenas 1 casa antes da vírgula.")
    print("Ex: 1011110,11010 => 2^6 * 1,01111011010")
    print("Ex: 1100000111,01 => 2^9 * 1,10000011101")
    print( n, "=", binarioComVirgula, "= 2^", (len(binario) - precisao - 1), "*", binario[:1] + "," + binario[1:])
    print("\n3) Identifique o SINAL, o EXPOENTE, e a MANTISSA.\nSe o número é positivo, o sinal será 0, se for negativo será 1. O expoente é quantas casas andamos para a esquerda no passo 2), somado a um BIAS que é 127. A mantissa é todo o número restante depois da vírgula no passo 2), acrescentando zeros até ter 23 dígitos (assim, 23 + 8 + 1 = 32 bits da precisão simples)")
    sinal = 0 if n > 0 else 1
    expoente = 127 + (len(binario) - precisao - 1)
    mantissa = binario[1:]
    print("SINAL:", sinal)
    print("EXPOENTE: 127 + ", (len(binario) - precisao - 1), "=", expoente, "=", bin(expoente)[2:])
    print("MANTISSA:", mantissa.ljust( 23, "0" ))
    print("\nResposta:", sinal, "", bin(expoente)[2:], "", mantissa.ljust( 23, "0" ))
    print("          ^      ^               ^")
    print("        SINAL EXPOENTE        MANTISSA\n")       
    

print("Vamos aprender como representar um número pela norma IEEE 754")
print("Antes de começar, por favor, tenha em mente que a precisão deste programa é de 10 casas decimais. Se quiser mais, ou menos, modifique o script para tal.")

print("========================================")
while (True):
    num = float(input("Digite o número (Ex: 42.3): "))
    tutorial( num )
