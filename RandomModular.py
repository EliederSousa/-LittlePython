## 
#  RandomModular.py
#  
#  Copyright (c) 2020, Elieder Sousa
#  eliedersousa<at>gmail<dot>com
#  
#  Distributed under the MIT license.
#  
#  @date     23/09/20
#  
#  @brief       Gera números aleatórios através de uma função modular.
#               Perceba que se a semente inicial for 24, teremos uma sequência de 24,11,24,11...
##

import random

semente = random.randrange(0,9999)

def aleatorio():
    global semente
    semente = (11 * semente + 7) % 26
    return semente

for i in range(1, 11):
    print(i, ": ", aleatorio(), sep="")