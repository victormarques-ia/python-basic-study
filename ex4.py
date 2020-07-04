
"""
Fazer um programa para ler os dados de um funcionário (nome, salário bruto e imposto). Em
seguida, mostrar os dados do funcionário (nome e salário líquido). Em seguida, aumentar o
salário do funcionário com base em uma porcentagem dada (somente o salário bruto é
afetado pela porcentagem) e mostrar novamente os dados do funcionário. Use a classe
projetada abaixo.
"""

class Employee:
  name = ''
  grossSalary = 0.0
  tax = 0.0

  def netSalary(self):
    return (self.grossSalary - self.tax)
  
  def increaseSalary(self, percentage):
    self.grossSalary += (self.grossSalary * (percentage / 100))

  def __str__(self):
    return '{0}, $ {1:3.2f}'.format(self.name, self.netSalary())


def Main():

  employee = Employee() 

  employee.name = input('Name: ')
  employee.grossSalary = float(input('Gross salary: '))
  employee.tax = float(input('Tax: '))

  print(f'Employee: {employee}')

  employee.increaseSalary(float(input('Which percentage to increase salary? ')))

  print(f'Updated data: {employee}')



if __name__ == "__main__":
  Main()