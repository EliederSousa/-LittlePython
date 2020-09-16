## 
#  ExemploDeHash.py
#  
#  Copyright (c) 2020, Elieder Sousa
#  eliedersousa<at>gmail<dot>com
#  
#  Distributed under the MIT license.
#  
#  @date     16/09/20
#  
#  @brief       Calcula o hash de um número usando a função modular.
#               O algoritmo soma os valores numéricos das letras ( A-Z -> 0-26 ), e calcula o resultado mod N (fornecido pelo usuário).
##

def hash( nome, modNumber ):
    nome = nome.lower()
    tmpHash = ""
    for i in nome:
        tmpHash += str(ord(i)-97).zfill(2)

    print('Hash de "', nome, '" : ', int(tmpHash) % modNumber, sep="")


while ( True ):
    hash(input("Digite a palavra sem números, simbolos, e espaços: "), int(input("Digite o número para calcular o módulo [maior que 0]: ")) ) 