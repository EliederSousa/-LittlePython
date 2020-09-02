## 
#  Algoritmo de Euclides (MDC).py
#  
#  Copyright (c) 2020, Elieder Sousa
#  eliedersousa<at>gmail<dot>com
#  
#  Distributed under the MIT license.
#  
#  @date     02/09/20
#  
#  @brief   Algoritmo de Euclides
#           Retorna o MDC entre dois números.
##

def mdc( x, y ):
    if ( y == 0 ):
        return x
    else:
        return mdc( y, x % y )

print("Vamos calcular o MDC de dois números pelo Algoritmo de Euclides.")
while (True):    
    A = int(input("Entre com o 1º número: "))
    B = int(input("Entre com o 2º número: "))
    print( "O MDC de", A, "e", B, "é:", mdc( A, B ) )
    print("------------------------------")