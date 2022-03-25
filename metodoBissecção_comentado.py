"""
"  metodoBisseccao_comentado.py
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

import math

# Devido a complexidade de se criar uma função que generalize o cálculo de qualquer tipo de equação
# nos restringimos a calcular apenas polinômios, por serem de fácil representação.
def calculateEquation( func, x ):
    # Definimos que cada índice na lista representa um grau de um polinômio, a começar do maior pro menor
    sum = 0;
    for w in range(len(func)):
        sum += func[w] * (x ** ((len(func)-1)-w))
    return sum
    
    
def bisseccao( f, a, b, epsilon ):
    maxIterations = 100
    
    for iteration in range( 0, maxIterations ):
        p = (a + b) / 2
        fa = calculateEquation( f, a )
        fb = calculateEquation( f, b )
        fp = calculateEquation( f, p )
        
        print("Intervalo {}, temos:".format(iteration+1))
        print("Para a = {}, f({}) = {}".format(a, a, fa))
        print("Para b = {}, f({}) = {}".format(b, b, fb))
        print("Para p = {}, f({}) = {}".format(p, p, fp))
        
        
        
        if (fp == 0) or (abs(fp) < epsilon):
            print("fp é menor que a tolerância")
            return p
        
        if fa * fp > 0:
            print("f(a).f(p) > 0")
            a = p
        else:
            print("f(a).f(p) < 0")
            b = p
        print("----------------------------------------")
    
    print( "Erro: número máximo de iterações alcançado." )
    return 0;

print(bisseccao([1, -3, 1, 1, 1], .5, 1.5, 0.01))