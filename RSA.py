## 
#  RSA.py
#  
#  Copyright (c) 2020, Elieder Sousa
#  eliedersousa<at>gmail<dot>com
#  
#  Distributed under the MIT license.
#  
#  @date     30/09/20
#  
#  @brief    Codificação RSA para estudo. Não aceita espaços, nem números, apenas letras.
##

# Melhor forma que encontrei, achei no StackOverflow.
def wrap ( texto, tamanho ):
    return [texto[i:i + tamanho] for i in range(0, len(texto), tamanho)]

def stringfy( texto ):
    lista = wrap(texto, 2)
    r = []
    a = 0
    for w in lista:
        r.append("")
        for i in w:
            r[a] += str(ord(i.lower())-97).zfill(2)
        a += 1
    return r

def RSAEncode ( numList ):
    r = []
    a = 0
    for i in numList:
        r.append( str((int(i) ** c) % (p1 * p2)).zfill(4) )
    return r

# Variáveis globais que guardam P1 e P2 (primos) e C (expoente). Use P1, P2 e C pequenos
# Pois o script não tem nenhuma otimização para o processo.
p1  = 43
p2  = 59
c   = 13

print("p1: ", p1, "\np2: ", p2, "\np1*p2: ", p1 * p2, "\nc:  ", c)
while (True):    
    nome = input("Digite o texto [ex: siga]: ")
    print( "Separando por pares:", wrap( nome, 2 ))
    print( "Extraindo suas representações numéricas:", stringfy( nome ))
    print( "Codificado:", RSAEncode( stringfy(nome) ) )
    
