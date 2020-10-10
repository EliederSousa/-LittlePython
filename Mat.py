def code( text ):
    b = ""
    for i in text:
        b += str(ord(i.lower())-97).zfill(2)
    return b

def f( x ):
    return str((p*p*x - q) % 173).zfill(3)

# Extrai o MDC pelo Algoritmo de Euclides
def mdc( x, y ):
  if y == 0:
      return x
  else:
      return mdc(y, x % y)

# Retorna o inverso através de uma combinação linear (via brute-force)
def inversoMultiplicativo( a, b ):
    if mdc( a, b ) != 1:
        return "não existe!"
    x = 1
    y = 1
    while( ((x*a) % (b*y)) != 1 ):
        x += 1
        if (x * a) > (y + 1) * b:
            y += 1

    return x

def bin( x ):
    return format(x, "b")
    
print("Para verificar as respostas, criei este script.\nPor questões de ética com a prova, não postei antes\nmas estou fazendo-o agora (09/10/2020, 23:55)\npara você tirar sua curiosidade com as respostas.")
print("Use este script como um aprendizado em Python; dá pra aprender muita coisa aqui!")

TIA = int(input("Digite seu TIA: "))
p = (TIA % 10) + 2
q = (TIA % 100 // 10) + 3
nome = input("Digite seu primeiro nome: ")
r = int(code(nome)) % 101

# [0]
print("\nQuestão [0]")
print("{0} --> {1} mod 101 --> r = {2}".format(nome, code(nome), r))
print("p = {0} + 2 = {1}".format(TIA % 10, p))
print("q = {0} + 3 = {1}".format(TIA % 100 // 10, q))

# [1]
print("\nQuestão [1]")
print("X Y Z    X ∩ Y    X ∩ Z    ( X ∩ Y ) U ( X ∩ Z )    [( X ∩ Y ) U ( X ∩ Z )]ᶜ")
for i in range(7, -1, -1):
    x = i >> 2 & 1
    y = i >> 1 & 1
    z = i & 1
    xory = x & y
    xorz = x & z
    xoryandxorz = xory | xorz
    negatexoryandxorz = int( not xoryandxorz )
    print("{0} {1} {2}      {3}        {4}                {5}                         {6}".format(x, y, z, xory, xorz, xoryandxorz, negatexoryandxorz))
    
# [2]
print("\nQuestão [2]")
mdcResultado2 = mdc(p*(q+r), q*(p+r))
print("MDC({0}, {1}) =".format(p*(q+r), q*(p+r)), mdcResultado2)

# [3]
print("\nQuestão [3]")
mdcResultado3 = mdc(p*q+r, 449)
print("MDC({0}, 449) =".format(p*q+r), mdcResultado3)
print("Inverso da classe [{0}]_449 =".format(p*q+r), inversoMultiplicativo(p*q+r, 449))

# [4]
print("\nQuestão [4]")
x = p
print("X0 =", x)
for i in range(1, 6):
    y = x
    x = (q*x + r) % 223
    print( "X{0} = ({1} * {2} + {3}) mod 223 = {4} mod 223 = {5}".format(i, q, y, r, q*y+r, x))
    
# [5] a)
print("\nQuestão [5]")
resultado = ""
for i in "PROVA":
    resultado += f(int(code(i)))
print( "a)", resultado )

# [5] b)
# Calcula o Alpha primeiro.
ALPHA = inversoMultiplicativo(p*p, 173)
# Resposta:
print( "b)", "g(x) =", ALPHA, "x +", ALPHA*q , "mod 173" )

input("\n\nFinalizado. Se não conseguir ver todas as respostas, role a página para cima!\nPressione qualquer tecla para sair...")

