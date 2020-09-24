# Calcula o número de registro do usuário, problema da lista de exercícios para entrega.
def registro( nome, data ):
    reg = ""
    k = ""

    reg += str(int(data) % 71)
    
    for i in nome:
        k += str(ord(i.lower()) - 97).zfill(2)

    reg += str(int(k) % 937).zfill(3)
    return reg


while ( True ):
    A = input("Digite o sobrenome: ")
    B = input("Digite a data de nascimento no formato DDMMAAAA: ")
    print(registro( A, B ))
