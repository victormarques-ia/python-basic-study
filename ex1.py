
"""
Fazer um programa para ler as medidas dos lados de dois triângulos X e Y (suponha medidas
válidas). Em seguida, mostrar o valor das áreas dos dois triângulos e dizer qual dos dois triângulos
possui a maior área.
"""

import math

class Triangle:

  a = 0
  b = 0
  c = 0

  def calculateArea(self):
    
    p = (self.a + self.b + self.c) / 2

    return math.sqrt(p * ( p- self.a) * (p - self.b) * (p - self.c ))
  

def Main():

  triangle1 = Triangle()
  triangle2 = Triangle()

  triangle1.a, triangle1.b, triangle1.c = [float(x) for x in input('Enter the measures of Triangle 1: ').split()]

  triangle2.a, triangle2.b, triangle2.c = [float(x) for x in input('Enter the measures of Triangle 2: ').split()]

  print('Triangle 1: ', triangle1.calculateArea())
  print('Triangle 2: ', triangle2.calculateArea())

  if (triangle1.calculateArea() > triangle2.calculateArea()):
    print('Triangl 1 is bigger')
  else:
    print('Triangle 2 is bigger')

if __name__=='__main__': 
  Main()   