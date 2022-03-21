"""
"  metodoBisseccao.py
"  
"  Copyright (c) 2022, Elieder Sousa
"  eliedersousa<at>gmail<dot>com
"  
"  Distributed under the MIT license.
"  
"  @date     18/03/22
"  
"  @brief    Aproxima uma raíz de uma equação de grau n, através do método da bissecção.
"""

# Devido a complexidade de se criar uma função que generalize o cálculo de qualquer tipo de equação
# nos restringimos a calcular apenas polinômios, por serem de fácil representação.
def calculateEquation( func, x ):
    # Definimos que cada índice na lista representa um grau de um polinômio, a começar do maior pro menor
    sum = 0;
    for w in range(len(func)):
        sum += func[w] * (x ** ((len(func)-1)-w))
    return sum


def bisseccao( f, a, b, epsilon ):
    maxIterations = 10
    
    for iteration in range( 0, maxIterations ):
        p = (a + b) / 2
        fa = calculateEquation( f, a )
        fp = calculateEquation( f, p )
        
        if (fp == 0) or (abs(fp) < epsilon):
            return p
        
        if fa * fp > 0:
            a = p
        else:
            b = p
    
    print( "Erro: número máximo de iterações alcançado." )
    return 0;
    
print(bisseccao([1, 4, 0, -10], 1, 2, 0.001))