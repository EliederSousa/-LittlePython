# Linear Congruential Generator
# http://people.duke.edu/~ccc14/sta-663-2016/15A_RandomNumbers.html

import random
import math

class LCG:
    def __init__( self, seed=random.random() ):
        self.m = 4294967296 # Because of modulus above, we need m as big enough.
        self.a = 1664525
        self.c = 1013904223
        self.z = 0

    def setSeed( self, seed ):
        if seed:
            self.seed = seed
        else:
            self.seed = random.random() * self.m
        self.z = self.seed

    def getSeed( self ):
        return self.seed
    
    def rand( self ):
        self.z = (self.a * self.z + self.c) % self.m
        return self.z / self.m # We return a number between 0 (inclusive) and 1: [0, 1)

class Noise:
    def __init__( self ):
        self.PERLIN_YWRAPB   = 4
        self.PERLIN_YWRAP    = 1 << self.PERLIN_YWRAPB
        self.PERLIN_ZWRAPB   = 8
        self.PERLIN_ZWRAP    = 1 << self.PERLIN_ZWRAPB
        self.PERLIN_SIZE     = 4095

        self.perlin_octaves = 4
        self.perlin_amp_falloff = 0.5

        self.perlin = [0] * (self.PERLIN_SIZE + 1)

        self.lcg = LCG()
        self.lcg.setSeed( random.randrange( 2**10, 2**20 ) )

        for x in range( self.PERLIN_SIZE + 1 ):
            self.perlin[x] = self.lcg.rand()

    def scaled_cosine( self, i ):
        return .5 * (1 - math.cos(math.pi * i))

    def translate(self, value, leftMin, leftMax, rightMin, rightMax):
        # Figure out how 'wide' each range is
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin

        # Convert the left range into a 0-1 range (float)
        valueScaled = float(value - leftMin) / float(leftSpan)

        # Convert the 0-1 range into a value in the right range.
        return rightMin + (valueScaled * rightSpan)

    def noise( self, x, y=0, z=0 ):
        x = abs(x)
        y = abs(y)
        z = abs(z)

        xi = math.floor(x)
        yi = math.floor(y)
        zi = math.floor(z)

        xf = x - xi
        yf = y - yi
        zf = z - zi

        r = 0
        ampl = .5

        for o in range( self.perlin_octaves ):
            of = xi + (yi << self.PERLIN_YWRAPB) + (zi << self.PERLIN_ZWRAPB)

            rxf = self.scaled_cosine(xf)
            ryf = self.scaled_cosine(yf)

            n1 = self.perlin[ of & self.PERLIN_SIZE ]
            n1 += rxf * ( self.perlin[ (of + 1) & self.PERLIN_SIZE ] - n1 )
            n2 = self.perlin[(of + self.PERLIN_YWRAP) & self.PERLIN_SIZE] 
            n2 += rxf * ( self.perlin[ (of + self.PERLIN_YWRAP + 1) & self.PERLIN_SIZE ] - n2 ) 
            n1 += ryf * (n2 - n1) 

            of += self.PERLIN_ZWRAP 
            n2 = self.perlin[of & self.PERLIN_SIZE] 
            n2 += rxf * (self.perlin[(of + 1) & self.PERLIN_SIZE] - n2) 
            n3 = self.perlin[(of + self.PERLIN_YWRAP) & self.PERLIN_SIZE] 
            n3 += rxf * (self.perlin[(of + self.PERLIN_YWRAP + 1) & self.PERLIN_SIZE] - n3) 
            n2 += ryf * (n3 - n2) 

            n1 += self.scaled_cosine(zf) * (n2 - n1) 
            r += n1 * ampl 
            ampl *= self.perlin_amp_falloff 
            xi <<= 1 
            xf *= 2 
            yi <<= 1 
            yf *= 2 
            zi <<= 1 
            zf *= 2 

            if (xf >= 1.0):
                xi += 1 
                xf -= 1 

            if (yf >= 1.0):
                yi += 1 
                yf -= 1 

            if (zf >= 1.0):
                zi += 1 
                zf -= 1 

        return r 

    def noiseDetail( self, lod, falloff ):
        if lod > 0:
            self.perlin_octaves = lod
        if falloff > 0:
            self.perlin_amp_falloff = falloff

    def noiseSeed( self, seed ):
        self.lcg.setSeed( seed )
        print(self.lcg.getSeed())
        for x in range( self.PERLIN_SIZE + 1 ):
            self.perlin[x] = self.lcg.rand()