## 
#  CifraDeCesar.py
#  
#  Copyright (c) 2020, Elieder Sousa
#  eliedersousa<at>gmail<dot>com
#  
#  Distributed under the MIT license.
#  
#  @date     21/09/20
#  
#  @brief    Codifica uma string usando a Cifra de Cesar.
## 
def cifraDeCesar( frase, deslocador ):
    frase = frase.lower()
    tmp = ""
    for i in frase:
        tmp += chr(((ord(i)+deslocador-97) % 26) + 97)

    print( tmp )


while ( True ):
    cifraDeCesar( input("Digite o texto: "), int(input("Digite o deslocamento [0-26]: ")) )