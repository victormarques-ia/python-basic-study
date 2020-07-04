"""
Fazer um programa para ler o nome de um aluno e as três notas que ele obteve nos três trimestres do ano
(primeiro trimestre vale 30 e o segundo e terceiro valem 35 cada). Ao final, mostrar qual a nota final do aluno no
ano. Dizer também se o aluno está aprovado (PASS) ou não (FAILED) e, em caso negativo, quantos pontos faltam
para o aluno obter o mínimo para ser aprovado (que é 60% da nota). Você deve criar uma classe Student para
resolver este problema.
"""


class Student:
  name = ''
  g1 = 0.0
  g2 = 0.0
  g3 = 0.0

  def finalGrade(self):
    return self.g1 + self.g2 + self.g3

  def finalAnwser(self):

    if (self.finalGrade() >= 60.0):

      print('Final grade: {0:3.2f}'.format(self.finalGrade()))
      print(self.name + ' PASS')

    else:
      print('Final grade: {0:3.2f}'.format(self.finalGrade()))
      print(self.name + ' FAILED')
      print('Missing: {0:3.2f} points'.format(60.00 - self.finalGrade()))



def Main():

  student = Student()

  student.name = input('Name: ')
  student.g1, student.g2, student.g3 = [float(x) for x in input("Enter the student's three grades: ").split()]

  student.finalAnwser()


if __name__ == "__main__":
  Main()

