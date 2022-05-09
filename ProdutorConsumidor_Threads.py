 ###
 #
 #  Elieder Damasceno Sousa       | 32093659
 #  José Eduardo Bernardino Jorge |42019877
 #
 ###
import threading,time,logging,random

lista = []
incremento = 0

def produtor():
    global lista
    for i in range(10):
      if len(lista) < 10 :
        lista.append(len(lista)+1)
        logging.info("Produtor produziu o valor.(%d)", len(lista))
        time.sleep(random.randrange(1,6))


def consumidor():
    global lista
    for i in range(10):
      if len(lista) > 0 :
        logging.info("Consumidor usou um item(%d).", lista.pop() )
        time.sleep(random.randrange(1,6))
      else:
        logging.info("Erro ao consumir, lista vazia!")        

format = "%(asctime)s - %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
num = 0

t1 = threading.Thread(target=produtor)
t2 = threading.Thread(target=consumidor)
t1.start()
t2.start()