"""
Fazer um programa para ler os dados de um produto em estoque (nome, preço e
quantidade no estoque). Em seguida:

• Mostrar os dados do produto (nome, preço, quantidade no estoque, valor total no
estoque)

• Realizar uma entrada no estoque e mostrar novamente os dados do produto

• Realizar uma saída no estoque e mostrar novamente os dados do produto
"""

class Product:
  name = ''
  price = 0.0
  quantity = 0

  def totalValueInStock(self):
    return self.price * self.quantity
  
  def addProducts(self, quantity):
    self.quantity += quantity
  
  def removeProducts(self, quantity):
    self.quantity -= quantity

  def __str__(self):
    return '{0}, $ {1:3.2f}, {2:2d} units, Total: $ {3:3.2f}'.format(
    self.name,
    self.price,
    self.quantity,
    self.totalValueInStock())

def Main():

  product = Product()

  print('Enter product data:')
  product.name = input('Name: ')
  product.price = float(input('Price: '))
  product.quantity = int(input('Quantity: '))

  print(f'Product data: {product}')

  product.addProducts(int(input('Enter the number of products to be added in stock: ')))

  print(f'Updated data: {product}')

  product.removeProducts(int(input('Enter the number of products to be removed from stock: ')))

  print(f'Updated data: {product}')


if __name__ == "__main__":
  Main()