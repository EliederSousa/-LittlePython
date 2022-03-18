"""
"  metodoJacobi.py
"  
"  Copyright (c) 2022, Elieder Sousa
"  eliedersousa<at>gmail<dot>com
"  
"  Distributed under the MIT license.
"  
"  @date     16/03/22
"  
"  @brief    Aproxima a solução de um sistema de equações lineares através do método de Jacobi.
"""

import math

n = int(input("Quantas equações/incógnitas exitem? "))
tolerancia = float(input("Digite a tolerância: "))
maxIteracoes = int(input("Digite o número máximo de iterações: "))

print("Digite as equações; uma equação por linha, separe as incógnitas por espaços.")

a = []
p = []
for w in range(0, n):
  print("\nDigite a {}ª equação (sem o resultado dela): ".format(w+1))
  a.append([float(k) for k in input().split(" ")])
  print("Qual é o resultado dela?")
  p.append(float(input()))

print("\nCalculando...\n")


s = [0] * n
w = 0
naochegounoresultado = True

while naochegounoresultado:
  print("{}ª interação".format(w+1))
  print("Matriz de aproximações:")
  for ap in range(0,len(s)):

    print("x{}({})".format(chr(8321+ap), w), "{:.4f}".format(s[ap]))
  temp = [0] * n
  erros = [0] * n
  
  for y in range( len(a) ): # pega a equação y
    print("x{}({}) = ".format(chr(8321+y), w+1), end='')
    for x in range( len(s) ): # pega a incognita x
      if x != y:
        temp[y] += (a[y][x]/-a[y][y])*s[x]
        print( " + (", a[y][x], "/", -a[y][y] , "*" , "{:.4f}".format(s[x]), ")", end='')
    temp[y] += p[y]/a[y][y]
    print( " + (", p[y], "/", a[y][y], ") = ", "{:.4f}".format(temp[y]))
    
    erros[y] = abs(temp[y] - s[y])
    
  print("Erro: ", format(erros))

  #Variáveis para calcular o criterio
  erro = max(erros)
  denominador = max(temp)
  print("O denominador do critério é {:.4f}".format( denominador))

  #Calculando o critério
  criterio = erro/denominador
  print("O critério é: {:.4f}".format(criterio))
  s = temp

  print("\n")
  
  if criterio < tolerancia:
    print("Sucesso!")
    naochegounoresultado = False
  elif w == maxIteracoes:
    print("Máximo de iterações excedidas! Criterio não atingiu a tolerância!")
    naochegounoresultado = False
    
  w += 1
