## 
#  Forma fatorada.py
#  
#  Copyright (c) 2020, Elieder Sousa
#  eliedersousa<at>gmail<dot>com
#  
#  Distributed under the MIT license.
#  
#  @date     04/09/20
#  
#  @brief    Calculando a forma fatorada (divisores primos) de um número inteiro.
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


# Função que pega os divisores primos de um número
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
	
# Função que pega os divisores únicos (e primos) de um número
def divisores( n, tabela ):
    t = 0
    div = []
    while( n > 1 ):
        if( n % tabela[t] == 0 ):
            div.append( tabela[t] )
            n /= tabela[t]
        else:
            t += 1
    return div

print("Aguarde a tabela de números primos ser criada...")
tabela = tabelaDePrimos( 2**14 )
print("...Pronto!")
print("Vamos calcular a forma fatorada de um número inteiro.")
while (True):
    A = int(input("Digite o número: "))
    print("Divisores:", divisores(A, tabela))