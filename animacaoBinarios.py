## 
#  animacaoBinarios.py
#  
#  Copyright (c) 2020, Elieder Sousa
#  eliedersousa<at>gmail<dot>com
#  
#  Distributed under the MIT license.
#  
#  @date     19/09/20
#  
#  @brief    Pequena animação que criei para um artigo, afim de mostrar os números binários de 0 até nMax.
## 
import time
import os

clear = lambda: os.system('cls')
nMax = 2**5
i = 0

while (True):
    
    clear() 
    print( str(i).zfill(3), "=", "{0:05b}".format(i) )
    i += 1
    if i == nMax:
        i = 0
    time.sleep(.25)