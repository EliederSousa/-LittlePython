"""
"  Cadeia de Markov.py
"  
"  Copyright (c) 2021, Elieder Sousa
"  eliedersousa<at>gmail<dot>com
"  
"  Distributed under the MIT license.
"  
"  @date     17/04/22
"  
"  @brief    Calcula a matriz de probabilidades dos momentos N para uma Cadeia de Marcov.
"""
import math

a = 0.7
b = 0.2
c = 0.1

peso = [[0.2, 0.2, 0.6],[0.3, 0, 0.7],[1, 0, 0]];

print("M0 = ")
print("A = {}".format(a))
print("B = {}".format(b))
print("C = {}\n".format(c))

for w in range(0, 4):
    
    tempA = round((a * peso[0][0]) + (b * peso[1][0]) + (c * peso[2][0]), 3)
    tempB = round((a * peso[0][1]) + (b * peso[1][1]) + (c * peso[2][1]), 3)
    tempC = round((a * peso[0][2]) + (b * peso[1][2]) + (c * peso[2][2]), 3)
    
    print("\nM{} = ".format(w+1))
    print("A = ({} * {}) + ({} * {}) + ({} * {}) = {}%".format(a, peso[0][0], b, peso[1][0], c, peso[2][0], round(tempA*100, 1)))
    print("B = ({} * {}) + ({} * {}) + ({} * {}) = {}%".format(a, peso[0][1], b, peso[1][1], c, peso[2][1], round(tempB*100, 1)))
    print("C = ({} * {}) + ({} * {}) + ({} * {}) = {}%".format(a, peso[0][2], b, peso[1][2], c, peso[2][2], round(tempC*100, 1)))
    
    a = tempA
    b = tempB
    c = tempC