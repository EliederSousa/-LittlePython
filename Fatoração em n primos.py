"""
"  Fatoração em N primos.py
"  
"  Copyright (c) 2021, Elieder Sousa
"  eliedersousa<at>gmail<dot>com
"  
"  Distributed under the MIT license.
"  
"  @date     24/05/21
"  
"  @brief    Uma pequena função que calcula (por força-bruta) se um determinado número pode ser formado pela multiplicação de N primos (dados).
"  
"  @example  Dados os primos [2,3,5] podemos dizer que 15 pode ser fatorado por 3.5 . O número 14 não pode, pois 14/2 = 7 (que não está na lista).
"  
"""


"""
"  @brief               Determina se um número N pode ser fatorado por uma lista de números primos em (e somente eles) em ordem crescente.
"                       N deve ser maior que o menor primo da lista.
"  
"  @param [int] n       O número que se quer verificar.
"  @param [int] primos  A lista de número primos para usar na verificação. OBS: Deve estar em ordem crescente.    
"  @return Bool         Retorna True, se o número n pode ser fatorado. Caso contrário, retorna False.
"                       Se N < 1, ou se N é menor que o menor primo da lista, ou se a lista estiver vazia, retorna False.
"
"""
def redutivel( n, primos ):
    
    if len(primos) == 0 or n < primos[0] or n < 1:
        return False
        
    i = 0
    while i < len(primos):
        primo = primos[i]
        if n % primo == 0:
            n = int(n / primo)
        else:
            i += 1
        if n == 1:
            return True
    return False


# Exemplo de uso:
n = [3,7,13]
for i in range(2, 83):
    print("{0} é redutivel por {1}?".format(i, n), redutivel(i, n))
