## 
#  Anel Inverso MOD N.py
#  
#  Copyright (c) 2020, Elieder Sousa
#  eliedersousa<at>gmail<dot>com
#  
#  Distributed under the MIT license.
#  
#  @date     09/09/20
#  
#  @brief    Retorna o inverso de um anel de inteiros mod N através de uma combinação linear (via brute-force)
##
 
# Extrai o MDC pelo Algoritmo de Euclides
def mdc( x, y ):
  if y == 0:
      return x
  else:
      return mdc(y, x % y)

# Retorna o inverso através de uma combinação linear (via brute-force)
def inversoMultiplicativo( a, b ):
    if mdc( a, b ) != 1:
        return "não existe!"
    x = 1
    y = 1
    while( ((x*a) % (b*y)) != 1 ):
        x += 1
        if (x * a) > (y + 1) * b:
            y += 1

    return x


print("Calculando o inverso multiplicativo de [A]_b")
while (True):
    A = int(input("Entre com o 1º número: "))
    B = int(input("Entre com o 2º número: "))
    print("O inverso de [A]_b é:", inversoMultiplicativo( A, B ))
    print("========================================")