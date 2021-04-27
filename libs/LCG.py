"""
"  LCG.py
"  
"  Copyright (c) 2021, Elieder Sousa
"  eliedersousa<at>gmail<dot>com
"  
"  Distributed under the MIT license.
"  
"  @date     27/04/21
"  
"  @brief   Linear congruential generator
"           https://en.wikipedia.org/wiki/Linear_congruential_generator
"           A linear congruential generator (LCG) is an algorithm that yields a sequence of
"           pseudo-randomized numbers calculated with a discontinuous piecewise linear equation. 
"           The method represents one of the oldest and best-known pseudorandom number generator algorithms.
"""
import time

class lcg():
    def __init__(self):
        self.z = int(time.time() * 343220541) % 4294967296
   
    def random( self ):
        self.z = (1664525 * self.z + 1013904223) % 4294967296
        return self.z / 4294967296