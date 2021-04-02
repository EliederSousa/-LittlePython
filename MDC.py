def MDC( x, y ):
    if x == y:
        return x
    elif x > y:
        return MDC( x - y, y )
    else:
        return MDC( y, x )

x = 33
y = 6
print("MDC({0}, {1}) = {2}".format( x, y, MDC(x, y) ))
