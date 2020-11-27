def fatorial( n ):
    if( n == 0 ): return 1
    return n * fatorial( n - 1 ) 

def binomial( n, k ):
    return int(fatorial(n) / ( fatorial(k) * fatorial(n - k) ))
    
    
def linhaBinomial( n ):
    coeficientes = []
    for w in range(n + 1):
        coeficientes.append(binomial(n, w))
    return coeficientes


for w in range( 0, 20 ):
    print(', '.join(map(str,linhaBinomial(w) )))
    
input()