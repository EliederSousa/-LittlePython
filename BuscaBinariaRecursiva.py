## 
#  BuscaBinariaRecursiva.py
#  
#  Copyright (c) 2021, Elieder Sousa
#  eliedersousa<at>gmail<dot>com
#  
#  Distributed under the MIT license.
#  
#  @date     19/04/21
#  
#  @brief    Implementação da busca binária, com recursividade.
##

## 
#  @brief Esta função implementa a busca binária, que é um algoritmo que procura por um elemento em um vetor.
#  Este método é mais rápido que um algoritmo de busca linear ( O(log_2 n) ).
#  
#  @param [list] vetor O vetor para ser procurado o elemento.
#  @param [int] n O elemento a ser procurado.
#  @param [int] menor O menor índice que se encontra particionado o vetor. É um helper para a recursividade.
#  @return Retorna o índice do vetor onde se encontra o elemento. Se o elemento não for encontrado, retorna -1.
#  
##
def buscaBinariaRecursiva( vetor, n, menor=0 ):
    meio = len(vetor)//2
    # print( "Vetor:", vetor, ", vetor[meio]:", vetor[meio], ", Menor:", menor, ", n:", n )
    if len(vetor) == 0:
        return -1
    elif vetor[meio] == n:
        return meio + menor
    elif vetor[meio] > n:
        return buscaBinariaRecursiva( vetor[:meio], n, menor)
    elif vetor[meio] < n:
        menorElemento = menor + (meio + 1)
        return buscaBinariaRecursiva( vetor[(meio+1):] , n, menorElemento)

print(buscaBinariaRecursiva([2,5,7,8,9,10,13,14,16,18,20], 16))