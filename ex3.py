"""
Fazer um programa para ler os valores da largura e altura
de um retângulo. Em seguida, mostrar na tela o valor de
sua área, perímetro e diagonal. Usar uma classe como
mostrado no projeto ao lado.
"""
import math

class Rectangle:
  width = 0.0
  height = 0.0

  def area(self):
    return self.width * self.height

  def perimeter(self):
    return (self.width * 2) + (self.height * 2)
  
  def diagonal(self):
    return math.sqrt((self.width ** 2) + (self.height ** 2))


def Main():

  rectangle = Rectangle()

  rectangle.width, rectangle.height = [float(x) for x in input('Enter rectangle width and height: ').split()]

  print('Area: % 3.2f' %(rectangle.area()))
  print('Perimeter: % 3.2f' %(rectangle.perimeter()))
  print('Diagonal: % 3.2f' %(rectangle.diagonal()))


if __name__ == "__main__":
  Main()