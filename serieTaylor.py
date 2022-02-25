"""
"  Série Taylor
"  
"  Copyright (c) 2022, Elieder Sousa
"  eliedersousa<at>gmail<dot>com
"  
"  Distributed under the MIT license.
"  
"  @date     24/02/22
"  
"  @brief    Função em Python que aproxima e^n através de séries de Taylor.
"""

import math

print("Serie de Taylor")

def serieTaylor( n ):
    precision = 20
    result = 1

    for w in range(1, precision):
        result += (n**w)/math.factorial(w)

    return result
    
while True:
    n = int(input("\nEntre com o valor de n para calcularmos e^n: "))
    print(serieTaylor( n ))
