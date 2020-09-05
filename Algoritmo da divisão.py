## 
#  Algoritmo da divisão.py
#  
#  Copyright (c) 2020, Elieder Sousa
#  eliedersousa<at>gmail<dot>com
#  
#  Distributed under the MIT license.
#  
#  @date     04/09/20
#  
#  @brief    Mostra a divisão entre dois números inteiros
##

print("Vamos calcular a divisão de dois números inteiros, pelo algoritmo da divisão.")
print("O resultado será na forma: D = Q * d + R")
print("Sendo: D = Dividendo")
print("       Q = Quociente")
print("       d = Divisor")
print("       R = Resto")
print("Exemplo: 84 / 17")
print("84 = 17 x 4 + 16")
print("========================================\n")
while (True):
    dividendo = int(input("Entre com o primeiro número (dividendo): "))
    divisor   = int(input("Entre com o segundo número (divisor): "))
    print(dividendo, "=", divisor, ".", dividendo // divisor, "+", dividendo % divisor, "-->", divisor, "não" if dividendo % divisor > 0 else "", "divide", dividendo )
    print("========================================\n")