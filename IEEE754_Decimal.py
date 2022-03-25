"""
"  IEEE754_Decimal.py
"  
"  Copyright (c) 2022, Elieder Sousa
"  eliedersousa<at>gmail<dot>com
"  
"  Distributed under the MIT license.
"  
"  @date     25/03/22
"  
"  @brief    Retorna o valor em decimal aproximado de um número em representação IEEE754.
"""

import math

def representacaoFloat( n ):
    #sinal = (-2 * int(n[0])) + 1 # graça kkk
    sinal = (-1) ** int(n[0])
    expoente = int(n[1:9], 2) - 127
    mantissa = n[9:]
    resultado = 2**expoente
    
    for w in range(0, len(mantissa) ):
        resultado += (2 ** ((expoente-1)-w)) * int(mantissa[w])
    
    print("Sinal:", sinal)
    print("Expoente:", expoente)
    print("Mantissa:", mantissa)
    print("Resultado = (-1)^sinal * 2^expoente-127 * (1+f):", sinal * resultado)
    
def representacaoDouble( n ):
    #sinal = (-2 * int(n[0])) + 1 # graça kkk
    sinal = (-1) ** int(n[0])
    expoente = int(n[1:12], 2) - 1023
    mantissa = n[12:]
    resultado = 2**expoente
    
    for w in range(0, len(mantissa) ):
        resultado += (2 ** ((expoente-1)-w)) * int(mantissa[w])
    
    print("Sinal:", sinal)
    print("Expoente:", expoente)
    print("Mantissa:", mantissa)
    print("Resultado = (-1)^sinal * 2^expoente-1023 * (1+f):", sinal * resultado)
	
	
representacaoFloat("01100000101000000000000000000000")