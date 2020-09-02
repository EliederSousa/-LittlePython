## 
#  Totient (phi) de Euler.py
#  
#  Copyright (c) 2020, Elieder Sousa
#  eliedersousa<at>gmail<dot>com
#  
#  Distributed under the MIT license.
#  
#  @date     02/09/20
#  
#  @brief    Calcula a função totiente (phi) de Euler
#
##

# Função que cria uma tabela de números primos
def tabelaDePrimos( max ):
    primos = [3,5]
    for x in range( 7, max, 2 ):
        if ( x % 5 == 0):
            continue
        else:
            for y in primos:
                temp = 0
                if ( x % y == 0 ):
                    temp = 1
                    break;
            if( temp == 0 ): primos.append( x )
    primos = [2] + primos
    return primos


# Função que pega os divisores primos (únicos) de um número
def divisoresUnicos( n, tabela ):
    t = 0
    div = []
    while( n > 1 ):
        if n % tabela[t] == 0:
            if not tabela[t] in div:
                div.append( tabela[t] )
            n /= tabela[t]
        else:
            t += 1
    return div

# Calcula a função totiente (phi) de Euler
def phi( n ):
    div = divisoresUnicos( n, tabela )
    phiTotal = n
    for w in div:
        phiTotal *= (1 - 1/w)
    return int(phiTotal)

print("Aguarde a tabela de números primos ser criada...")
tabela = tabelaDePrimos( 2**10 ) # Não precisamos mais do que isso em aula.
print("... Pronto!")
print("Vamos calcular o valor da função phi de Euler: ")
while (True):
    A = int(input("Digite o número: "))
    print("Phi(", A , ") é: ", phi(A))