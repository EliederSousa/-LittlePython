"""
"  InterpolacaoLagrange.py
"  
"  Copyright (c) 2022, Elieder Sousa
"  eliedersousa<at>gmail<dot>com
"  
"  Distributed under the MIT license.
"  
"  @date     06/05/22
"  
"  @brief    Tendo um conjunto de pares ordenados (x, y) de uma função polinomial, podemos descobrir
"            o valor y de um novo ponto, usando o método de interpolação por polinômios de Lagrange.
"""

numvar = int(input("Quantos pontos? "))
pontos = []

print("Digite o valor x, e o resultado da função f(x), separados por espaços. Ex:")
print("Para f(8.1) = 16.94410 , digite: ")
print("8.1 16.9441\n")

for w in range(0, numvar):
  print("Ponto {}: ".format((w+1)))
  pontos.append([float(x) for x in input().split(" ")])

print("\nAgora entre com o ponto x que deseja calcular a interpolação: ")
forecast = float(input())

resultado = []

print("\nCalculando os polinômios de Lagrange: \n")
for w in range(0, numvar):
  print("L{},{}(x) = ".format(chr(8320+numvar-1), chr(8320+w)), end="")
  # Numerador:
  numerador = ""
  for k in range(0, numvar):
    if k != w:
      numerador += "(x - {})".format(pontos[k][0])
      print("(x - {})".format(pontos[k][0]), end="")

  print(" / ", end="")
  # Denominador:
  denominador = 1
  for k in range(0, numvar):
    if k != w:
      print("({} - {})".format(pontos[w][0], pontos[k][0]), end="")
      denominador *= pontos[w][0] - pontos[k][0]
  
  resultado.append(round(denominador, 4))

  print(" = \n1/{} * ({})".format(round(denominador, 7), numerador))
  print("\n")

total = 0
print("P({}) = ".format(forecast))
for w in range(0, numvar):
  temp = 1
  numerador = ""
  print("{} * (1/{}) * ".format(pontos[w][1], resultado[w]), end="")
  for k in range(0, numvar):
    if k != w:
      temp *= forecast - pontos[k][0]
      print("({} - {})".format(forecast, pontos[k][0]), end="")

  print(" +")
  total += pontos[w][1] * (1/resultado[w]) * temp

print("\nResultado: P({}) = {:.7f}".format(forecast, total))

input("Pressione ENTER para sair...")